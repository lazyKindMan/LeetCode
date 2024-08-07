import json
import os
import random
import time
from collections import defaultdict

import requests
from tqdm import tqdm

from python.constants import (LEET_CODE_BACKEND, RECENT_SUBMISSIONS_QUERY, RECENT_AC_SUBMISSIONS_QUERY,
                              USER_PROFILE_QUESTIONS_QUERY, PROGRESS_SUBMISSIONS_QUERY, MY_SUBMISSION_DETAIL_QUERY,
                              SUBMIT_SUCCESS_RESULT, SUBMIT_BASIC_RESULT, SUBMIT_FAIL_RESULT,
                              TESTCASE_TEMPLATE_PYTHON_TESTCASES)
from python.utils import general_request, get_china_daily_time, format_question_id


def check_submission(user_slug: str, question_frontend_ids: set[str],
                     min_timestamp=None,
                     max_timestamp=None):
    def handle_response(response: requests.Response):
        result_dict = json.loads(response.text)['data']['recentSubmitted']
        if result_dict:
            for submit in result_dict:
                question_id = format_question_id(submit['question']['questionFrontendId'])
                if submit['status'] == "A_10" and question_id in question_frontend_ids:
                    t = submit['submitTime']
                    if t >= min_timestamp and (not max_timestamp or t < max_timestamp):
                        ans[question_id] = t
                if submit['submitTime'] < min_timestamp:
                    break

    if min_timestamp is None:
        min_timestamp = get_china_daily_time()
    ans = dict()
    general_request(LEET_CODE_BACKEND,
                    handle_response,
                    json={"operationName": "recentSubmissions", "variables": {"userSlug": user_slug},
                          "query": RECENT_SUBMISSIONS_QUERY})

    return ans


def check_accepted_submission(user_slug: str, min_timestamp=None, max_timestamp=None):
    def handle_response(response: requests.Response):
        result_dict = json.loads(response.text)['data']['recentACSubmissions']
        if result_dict:
            for submit in result_dict:
                t = submit['submitTime']
                if t < min_timestamp:
                    break
                print(submit)
                if not max_timestamp or t < max_timestamp:
                    (ans[format_question_id(submit['question']['questionFrontendId'])]
                     .append((submit["submissionId"], submit['question']["titleSlug"], "python3")))

    if min_timestamp is None:
        min_timestamp = get_china_daily_time()
    ans = defaultdict(list)
    general_request('https://leetcode.cn/graphql/noj-go/', handle_response,
                    json={"query": RECENT_AC_SUBMISSIONS_QUERY,
                          "variables": {"userSlug": user_slug},
                          "operationName": "recentAcSubmissions"})
    return ans


def check_accepted_submission_all(cookie: str, min_timestamp=None, max_timestamp=None):
    def handle_response(response: requests.Response):
        result_dict = json.loads(response.text)['data']['userProfileQuestions']
        return result_dict['questions'] if result_dict else []

    def handle_response_submissions(response: requests.Response):
        result_dict = json.loads(response.text)["data"]["submissionList"]
        for submit in result_dict["submissions"]:
            t = int(submit['timestamp'])
            if t < min_timestamp:
                break
            print(submit)
            if not max_timestamp or t < max_timestamp:
                ans[format_question_id(question_submit_info["frontendId"])].append(
                    (submit["id"], question_submit_info["titleSlug"], submit["lang"]))

    if min_timestamp is None:
        min_timestamp = get_china_daily_time()
    page_no, page_size = 0, 20
    ans = defaultdict(list)
    query = {"operationName": "userProfileQuestions",
             "variables": {"status": "ACCEPTED", "skip": page_no * page_size, "first": page_size,
                           "sortField": "LAST_SUBMITTED_AT", "sortOrder": "DESCENDING",
                           "difficulty": []},
             "query": USER_PROFILE_QUESTIONS_QUERY}
    questions = general_request(LEET_CODE_BACKEND, handle_response,
                                json=query,
                                cookies={"cookie": cookie})
    if not questions:
        return ans
    while questions and questions[-1]["lastSubmittedAt"] >= min_timestamp and (
            not max_timestamp or questions[-1]["lastSubmittedAt"] < max_timestamp):
        page_no += 1
        query["variables"]["skip"] = page_no * page_size
        questions.extend(general_request(LEET_CODE_BACKEND, handle_response,
                                         json=query,
                                         cookies={"cookie": cookie}))
    while questions and questions[-1]["lastSubmittedAt"] < min_timestamp or (
            max_timestamp is not None and questions[-1]["lastSubmittedAt"] >= max_timestamp):
        questions.pop()
    for question_submit_info in questions:
        general_request("https://leetcode.cn/graphql/", handle_response_submissions,
                        json={"operationName": "progressSubmissions",
                              "variables": {"offset": 0, "limit": 10,
                                            "questionSlug": question_submit_info["titleSlug"], },
                              "query": PROGRESS_SUBMISSIONS_QUERY},
                        cookies={"cookie": cookie})

    return ans


def get_submission_detail(submit_id: str, cookie: str, handle_fun=None):
    def handle_response(response: requests.Response):
        if not response.text:
            return None
        result_dict = json.loads(response.text)["data"]["submissionDetail"]
        if result_dict['statusDisplay'] != 'Accepted':
            # wrong solution, add testcase
            return {
                "statusDisplay": result_dict["statusDisplay"],
                "input": result_dict["outputDetail"]["input"],
                "output": result_dict["outputDetail"]["expectedOutput"]
            }
        return {
            "statusDisplay": result_dict["statusDisplay"],
            "code": result_dict["code"],
            "lang": result_dict["lang"],
            "runtime": result_dict["runtimeDisplay"],
            "rawMemory": result_dict["memory"],
            "timestamp": result_dict["timestamp"],
        }

    if handle_fun is None:
        handle_fun = handle_response

    return general_request(LEET_CODE_BACKEND, handle_fun,
                           json={"operationName": "submissionDetails",
                                 "variables": {"submissionId": submit_id},
                                 "query": MY_SUBMISSION_DETAIL_QUERY},
                           cookies={"cookie": cookie})


def _add_test(root_path, problem_folder: str, question_id: str, code_input: str, expected_output: str):
    need_add_test = True
    code_input_py = code_input.replace("null", "None").replace("true", "True").replace("false", "False")
    expected_output_py = expected_output.replace("null", "None").replace("true", "True").replace("false", "False")
    if "\n" in code_input_py:
        code_input_py = code_input_py.replace("\n", ",")
        code_input_py = f"[{code_input_py}]"

    file_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}", "testcase.py")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().split("\n")
        for line in content:
            if "self.testcases.append(case(Input=" in line:
                splits = line.split(", Output=")
                ipt, opt = splits[0].split("=")[-1].strip(), splits[-1].strip()[:-2]
                if (ipt.replace(" ", "") == code_input_py.replace(" ", "") or
                    ipt.replace(" ", "").replace("'", "\"") == code_input_py.replace(" ", "")) and \
                        opt.replace(" ", "") == expected_output_py.replace(" ", ""):
                    need_add_test = False
                    break
    if need_add_test:
        new_content = []
        add_line = False
        for line in content:
            if line.strip().startswith("self.testcases.append(case(Input="):
                add_line = True
            elif add_line:
                new_content.append(
                    TESTCASE_TEMPLATE_PYTHON_TESTCASES.format(code_input_py, expected_output_py).replace("\n", ""))
                add_line = False
            new_content.append(line)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(new_content))

    need_add_test = True
    file_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}", "testcase")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().split("\n")
            code_input = code_input.replace("\n", "\\n").replace("\"", "\\\"")
            if f"\"{code_input}\"".replace(" ", "") in content[0].replace(" ", "") \
                    and expected_output.replace(" ", "") in content[1].replace(" ", ""):
                need_add_test = False
        if need_add_test:
            new_content = "\n".join([content[0][:-1] + ", \"{}\"]".format(code_input),
                                     content[1][:-1] + f", {expected_output}]"])
            with open(file_path, 'w', encoding="utf-8") as f:
                f.write(new_content)


async def submit_code(root_path, problem_folder: str, question_id: str, question_slug: str, cookie: str, lang: str,
                      leetcode_question_id: str, typed_code: str, study_plan_slug: str = None) -> dict | None:
    def handle_submit_response(response: requests.Response):
        if not response.text or response.status_code != 200:
            print(response.status_code, response.text)
            return None
        result_dict = json.loads(response.text)
        return result_dict["submission_id"]

    def handle_submit_check_response(response: requests.Response):
        if not response.text or response.status_code != 200:
            print(response.status_code, response.text)
            return False
        result_dict = json.loads(response.text)
        return result_dict["state"] == "SUCCESS"

    def handle_submit_detail_response(response: requests.Response):
        if not response.text or response.status_code != 200:
            print(response.status_code, response.text)
            return None
        result_dict = json.loads(response.text)["data"]["submissionDetail"]
        return {
            "statusDisplay": result_dict["statusDisplay"],
            "outputDetail": result_dict["outputDetail"],
            "memory": result_dict["memory"],
            "memoryDisplay": result_dict["memoryDisplay"],
            "memoryPercentile": result_dict["memoryPercentile"],
            "runtimeDisplay": result_dict["runtimeDisplay"],
            "runtimePercentile": result_dict["runtimePercentile"],
            "passedTestCaseCnt": result_dict["passedTestCaseCnt"],
            "totalTestCaseCnt": result_dict["totalTestCaseCnt"],
            "code": result_dict["code"],
            "lang": result_dict["lang"],
            "timestamp": result_dict["timestamp"],
        }

    submit_request_json = {"lang": lang,
                           "question_id": leetcode_question_id,
                           "typed_code": typed_code}
    if study_plan_slug:
        submit_request_json["study_plan_slug"] = study_plan_slug
    submit_id = general_request(f"https://leetcode.cn/problems/{question_slug}/submit/", handle_submit_response,
                                json=submit_request_json,
                                cookies={"cookie": cookie},
                                headers={"Origin": "https://leetcode.cn"})
    if not submit_id:
        return None
    submit_success = False
    for _ in tqdm(range(50)):
        if general_request(f"https://leetcode.cn/submissions/detail/{submit_id}/check/",
                           handle_submit_check_response,
                           cookies={"cookie": cookie},
                           headers={"Origin": "https://leetcode.cn"}):
            submit_success = True
            break
        time.sleep(random.randint(200, 300) / 1000)
    if not submit_success:
        return None
    submit_detail = get_submission_detail(submit_id, cookie, handle_submit_detail_response)
    if submit_detail is None:
        return None
    if submit_detail["statusDisplay"] == "Accepted":
        part = SUBMIT_SUCCESS_RESULT.format(
            submit_detail["runtimeDisplay"],
            submit_detail["runtimePercentile"],
            submit_detail["memoryDisplay"],
            submit_detail["memoryPercentile"]
        )
    else:
        part = SUBMIT_FAIL_RESULT.format(
            submit_detail["outputDetail"]["input"],
            submit_detail["outputDetail"]["codeOutput"],
            submit_detail["outputDetail"]["expectedOutput"],
            submit_detail["outputDetail"]["compileError"],
            submit_detail["outputDetail"]["runtimeError"],
        )
        if submit_detail["outputDetail"]["input"] and submit_detail["outputDetail"]["expectedOutput"]:
            _add_test(root_path, problem_folder, question_id,
                      submit_detail["outputDetail"]["input"], submit_detail["outputDetail"]["expectedOutput"])

    print(SUBMIT_BASIC_RESULT.format(
        submit_detail["statusDisplay"],
        submit_detail["passedTestCaseCnt"],
        submit_detail["totalTestCaseCnt"],
        part,
        typed_code
    ))
    return submit_detail
