import json
import traceback
import requests
import markdown
import html2text
from typing import Optional


def get_question_info(slug: str) -> Optional[dict]:
    try:
        result = requests.post("https://leetcode.cn/graphql/",
                               json={"query": "\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug:"
                                              " $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n"
                                              "    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n"
                                              "    categoryTitle\n  }\n}\n    ",
                                     "variables": {"titleSlug": slug},
                                     "operationName": "questionTitle"})
        res_dict = json.loads(result.text)['data']['question']
        return {
            "title": res_dict['title'],
            "difficulty": res_dict['difficulty'],
            "questionFrontendId": res_dict['questionFrontendId'],
        }
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def get_question_desc(slug: str, cookie: Optional[str] = None) -> Optional[str]:
    try:
        cookies = dict()
        if cookie:
            cookies['cookie'] = cookie
        result = requests.post("https://leetcode.cn/graphql/",
                               json={
                                   "query": "\n    query questionContent($titleSlug: String!) {\n  "
                                            "question(titleSlug: $titleSlug) {\n    content\n    editorType\n    "
                                            "mysqlSchemas\n    dataSchemas\n  }\n}\n    ",
                                   "variables": {"titleSlug": slug},
                                   "operationName": "questionContent"},
                               cookies=cookies)
        res_dict = json.loads(result.text)
        return res_dict['data']['question']['content']
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def extract_outputs_from_md(markdown_text: str) -> list:
    res = []
    splits = markdown_text.split("Output")
    for i in range(1, len(splits)):
        tmp = (splits[i].split("\n")[0].split(">")[-1]
               .replace("null", "None")
               .replace("true", "True")
               .replace("false", "False")
               )
        tmp = tmp.strip()
        try:
            if len(tmp) > 0:
                res.append(eval(tmp))
            else:
                tmp = (splits[i].split("\n")[1].split(">")[-1]
                       .replace("null", "None")
                       .replace("true", "True")
                       .replace("false", "False"))
                res.append(eval(tmp))
        except SyntaxError as sxe:
            print(f"Syntax error: {sxe}")
            traceback.print_exc()
            # 将Markdown转换为HTML
            html_content = markdown.markdown(tmp)

            # 将HTML转换为字符
            text_content = html2text.html2text(html_content)
            res.append(eval(text_content))
    return res


def get_question_code(slug: str, cookie: Optional[str] = None) -> Optional[str]:
    try:
        cookies = dict()
        if cookie:
            cookies['cookie'] = cookie
        result = requests.post("https://leetcode.cn/graphql",
                               json={
                                   "query": "\n    query questionEditorData($titleSlug: String!) {\n  "
                                            "question(titleSlug: $titleSlug) {\n    questionId\n    "
                                            "questionFrontendId\n    codeSnippets {\n      lang\n      langSlug\n      "
                                            "code\n    }\n    envInfo\n    enableRunCode\n    hasFrontendPreview\n    "
                                            "frontendPreviews\n  }\n}\n    ",
                                   "variables": {"titleSlug": slug},
                                   "operationName": "questionEditorData"},
                               cookies=cookies)
        res_dict = json.loads(result.text)
        code_snippets = res_dict['data']['question']['codeSnippets']
        for cs in code_snippets:
            if cs["langSlug"] == "python3":
                return cs["code"]
        return None
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def get_question_testcases(slug: str) -> Optional[list]:
    try:
        result = requests.post("https://leetcode.cn/graphql",
                               json={"query": "\n    query consolePanelConfig($titleSlug: String!) {\n"
                                              "  question(titleSlug: $titleSlug) {\n    questionId\n"
                                              "    questionFrontendId\n    questionTitle\n    enableRunCode\n    "
                                              "enableSubmit\n    enableTestMode\n    jsonExampleTestcases\n    "
                                              "exampleTestcases\n    metaData\n    sampleTestCase\n  }\n}\n    ",
                                     "variables": {"titleSlug": slug},
                                     "operationName": "consolePanelConfig"})
        res_dict = json.loads(result.text)
        ans = []
        json_testcase = json.loads(res_dict["data"]["question"]["jsonExampleTestcases"])
        for item in json_testcase:
            input_strs = item.replace("null", "None").split("\n")
            if len(input_strs) == 1:
                ans.append(eval(input_strs[0]))
            else:
                ans.append([eval(i) for i in input_strs])
        return ans
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None


def get_questions_by_key_word(keyword: Optional[str],
                              fetch_all: bool = False,
                              premium_only: bool = False) -> Optional[list]:
    try:
        ans = []
        page_size, page_no = 50, 0
        while True:
            filters = dict()
            if keyword:
                filters["searchKeywords"] = keyword
            if premium_only:
                filters["premiumOnly"] = premium_only
            result = requests.post("https://leetcode.cn/graphql",
                                   json={"query": "\n    query problemsetQuestionList("
                                                  "$categorySlug: String, $limit: Int, $skip: Int, $filters: "
                                                  "QuestionListFilterInput) {\n  problemsetQuestionList(\n    "
                                                  "categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n"
                                                  "    filters: $filters\n  ) {\n    hasMore\n    total\n    "
                                                  "questions {\n      acRate\n      difficulty\n      freqBar\n      "
                                                  "frontendQuestionId\n      isFavor\n      paidOnly\n      "
                                                  "solutionNum\n      status\n      title\n      titleCn\n      "
                                                  "titleSlug\n      topicTags {\n        name\n        nameTranslated\n"
                                                  "        id\n        slug\n      }\n      extra {\n        "
                                                  "hasVideoSolution\n        topCompanyTags {\n          imgUrl\n     "
                                                  "     slug\n          numSubscribed\n        }\n      }\n    }\n  "
                                                  "}\n}\n    ",
                                         "variables": {"categorySlug": "all-code-essentials",
                                                       "skip": page_no * page_size, "limit": page_size,
                                                       "filters": filters},
                                         "operationName": "problemsetQuestionList"})
            res_dict = json.loads(result.text)["data"]["problemsetQuestionList"]
            ans.extend(res_dict["questions"])
            if not res_dict["hasMore"] or not fetch_all:
                break
            page_no += 1
        return ans
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return None
