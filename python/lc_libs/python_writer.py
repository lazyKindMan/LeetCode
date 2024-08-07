import inspect
import os
import time
import traceback
from collections import defaultdict, deque
from importlib.util import spec_from_file_location, module_from_spec

from python.constants import TESTCASE_TEMPLATE_PYTHON, TESTCASE_TEMPLATE_PYTHON_TESTCASES, SOLUTION_TEMPLATE_PYTHON
from python.lc_libs.language_writer import LanguageWriter
from python.utils import back_question_id


class Python3Writer(LanguageWriter):
    solution_file = "solution.py"
    test_file_path = "python/test.py"
    tests_file_paths = ["python/tests.py"]

    def change_test(self, content: str, problem_folder: str, question_id: str) -> str:
        ans = []
        for line in content.split("\n"):
            if line.startswith("QUESTION = "):
                ans.append(f'QUESTION = "{question_id}"')
                continue
            ans.append(line)
        return "\n".join(ans)

    def change_tests(self, content: str, problem_ids_folders: list, idx: int = 0) -> str:
        ans = []
        for line in content.split("\n"):
            if line.startswith("QUESTIONS ="):
                line = "QUESTIONS = {}".format(problem_ids_folders)
            ans.append(line)
        return "\n".join(ans)

    def write_solution(self, code_template: str, code: str = None, problem_id: str = "",
                       problem_folder: str = "") -> str:
        try:
            cs_map, defined_class, rest = Python3Writer.__process_code(code_template)
            modify_in_place = "Do not return anything" in code_template
            if len(cs_map) == 1:
                import_libs, process_input = (Python3Writer.
                                              __finalize_solution_code_with_single_class(cs_map, modify_in_place))
            else:
                import_libs, process_input = Python3Writer.__finalize_solution_code_complex(cs_map, modify_in_place)
            if code:
                # submission code, not template code
                if "class Solution" in code:
                    last_part = "\n".join(code.split("class Solution")[-1].split("\n")[1:])
                else:
                    last_part = code
            else:
                last_part = ("" if not rest or "(self" in rest[0] else "\n") + "\n".join(rest)
            return SOLUTION_TEMPLATE_PYTHON.format(
                "".join(import_libs) + ("\n" if import_libs and defined_class else "") +
                (("\n" if defined_class else "") + "\n".join(defined_class) + ("\n" if defined_class else "")),
                process_input,
                last_part
            )
        except Exception as e:
            print("Exception raised:", e)
            traceback.print_exc()
        return Python3Writer.__write_solution_python_backup(code_template)

    def get_solution_code(self, root_path, problem_folder: str, problem_id: str) -> (str, str):
        if not problem_id:
            with open(os.path.join(root_path, "python", "test.py"), "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip().startswith("QUESTION ="):
                        problem_id = line.split("=")[-1].strip().replace('"', '')
                        break
        if not problem_id:
            return "", problem_id
        file_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{problem_id}", "solution.py")
        if not os.path.exists(file_path):
            return "", problem_id
        final_codes = deque([])
        solve_part = False
        class_part = False
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            skip_solution = "from python.object_libs import " in content and " call_method" in content
            lines = content.split("\n")
            for line in lines:
                if line.startswith("import") or line.startswith("from "):
                    continue
                if "class Solution(solution.Solution):" in line:
                    if not skip_solution:
                        final_codes.append("class Solution:")
                    continue
                if "class Node:" in line or "class ListNode:" in line or "class TreeNode" in line:
                    class_part = True
                    continue
                if class_part:
                    if line.strip() == '' or line.startswith("class"):
                        class_part = False
                    else:
                        continue
                if "def solve(self, test_input=None):" in line:
                    solve_part = True
                    continue
                if solve_part:
                    if "return " in line:
                        solve_part = False
                    continue
                final_codes.append(line)
        while final_codes and final_codes[0].strip() == '':
            final_codes.popleft()
        return "\n".join(final_codes), problem_id

    @staticmethod
    def write_problem_md(question_id: str, question_name: str, desc: str) -> str:
        check = False
        formated = []
        for line in desc.split("\n"):
            if "<ul>" in line:
                check = True
            elif "</ul>" in line:
                check = False
            elif check and len(line) == 0:
                continue
            formated.append(line)
        return "# {}. {}\n\n{}".format(back_question_id(question_id), question_name, "\n".join(formated))

    @staticmethod
    def write_testcase(testcases, outputs) -> str:
        res = ""
        for inputs, output in zip(testcases, outputs):
            res += (TESTCASE_TEMPLATE_PYTHON_TESTCASES
                    .format(f"\"{inputs}\"" if isinstance(inputs, str) else inputs,
                            f"\"{output}\"" if isinstance(output, str) else output))
        return TESTCASE_TEMPLATE_PYTHON.format(res)

    @staticmethod
    def __get_code_class(tmp_filename):
        include_solution_class = False
        solution_spec = spec_from_file_location("module.name", tmp_filename)
        solution = module_from_spec(solution_spec)
        solution_spec.loader.exec_module(solution)
        classes = inspect.getmembers(solution, inspect.isclass)
        your_classes = [c for c in classes if c[1].__module__ == solution.__name__]

        cs_map = defaultdict(list)
        for cs in your_classes:
            class_name = cs[0]
            # Get the method of your class
            methods = inspect.getmembers(cs[1], inspect.isroutine)

            # Filter out in-built dunder methods
            non_dunder_methods = [
                m for m in methods
                if m[0] == "__init__" or not (m[0].startswith('__') and m[0].endswith('__'))]

            for method in non_dunder_methods:
                md = getattr(cs[1], method[0])
                sig = inspect.signature(md)
                if cs[0] == "Solution" and method[0] == "__init__":
                    d = dict(sig.parameters)
                    counts = len(d)
                    if "self" in d:
                        counts -= 1
                    if "args" in d:
                        counts -= 1
                    if "kwargs" in d:
                        counts -= 1
                    if counts == 0:
                        continue
                    if class_name in cs_map:
                        cs_map["S"] = list(cs_map[class_name])
                        cs_map.pop(class_name)
                    class_name = "S"
                    include_solution_class = True
                cs_map[class_name].append((method[0], dict(sig.parameters), sig.return_annotation))

        return cs_map, include_solution_class

    @staticmethod
    def __process_code(code: str):
        class_defines = []
        rest = []
        process_class = False
        splits = code.split("\n")
        idx = 0
        while idx < len(splits):
            line = splits[idx]
            if "# class " in line:
                process_class = True
                class_defines.append(line[2:])
                idx += 1
                continue
            elif process_class:
                if line.startswith("#"):
                    class_defines.append(line[2:])
                    idx += 1
                    continue
                else:
                    process_class = False
            if ('"""' in line and idx < len(splits) - 1 and
                    (splits[idx + 1].strip().startswith("class ") or splits[idx + 1].strip().startswith("# "))):
                idx += 1
                while idx < len(splits) and '"""' not in splits[idx]:
                    if "from typing import " not in rest:
                        class_defines.append(splits[idx])
                    idx += 1
                idx += 1
                continue
            if "from typing import " in line:
                idx += 1
                continue
            sl = line.strip()
            if sl and not sl.startswith("#"):
                rest.append(line)
            if sl.startswith("def ") and sl.endswith(":"):
                if idx < len(splits) - 1 and '"""' in splits[idx + 1]:
                    idx += 1
                    while idx < len(splits) - 1 and '"""' not in splits[idx + 1].strip():
                        rest.append(splits[idx])
                        idx += 1
                    rest.append(splits[idx])
                    idx += 1
                    rest.append(splits[idx])
                    sp = splits[idx].count(" ", None, splits[idx].index('"""'))
                    sp = ((sp + 3) // 4) * 4
                else:
                    sp = line.count(" ", line.index("def "))
                    sp = ((sp + 3) // 4) * 4 + 4
                rest.append(sp * " " + "pass")
                rest.append("")
            idx += 1
        tmp_filename = "tmp-{}.py".format(time.time())
        try:
            with open(tmp_filename, "w", encoding="utf-8") as f:
                f.writelines("from typing import *\n\n")
                f.writelines("\n".join(class_defines) + "\n\n")
                f.writelines("\n".join(rest))
            cs_map, include_solution = Python3Writer.__get_code_class(tmp_filename)
            if include_solution:
                for i, line in enumerate(rest):
                    if "class Solution" in line:
                        rest[i] = line.replace("Solution", "S")
            simply = []
            last_space = 0
            in_comment = 0
            for line in rest:
                if "class Solution" in line:
                    continue
                strip_line = line.strip()
                if strip_line.startswith('"""'):
                    in_comment ^= 1
                    simply.append(line)
                    continue
                if line.strip() == "pass":
                    simply.append(" " * (last_space + 4) + "pass")
                else:
                    simply.append(line)
                    if not in_comment:
                        last_space = len(line) - len(line.lstrip())
            rest = simply
        finally:
            if os.path.exists(tmp_filename):
                os.remove(tmp_filename)
        return cs_map, class_defines, rest

    @staticmethod
    def __calculate_parameters(parameters):
        count = len(parameters)
        if "self" in parameters:
            count -= 1
        if "args" in parameters:
            count -= 1
        if "kwargs" in parameters:
            count -= 1
        return count

    @staticmethod
    def __extract_process_input_from_method(cs_map, modify_in_place, import_libs, method):
        func_name, parameters, return_anno = method
        par_map = dict()
        add_lib = ""
        exists = False
        process_input = ""
        remain = ""
        inputs = ""
        is_first = True
        idx = 0
        for v in parameters.values():
            if v.name == "self":
                continue
            if v.name == "args":
                continue
            if v.name == "kwargs":
                continue
            par_map[v.name] = v.annotation
            if is_first:
                is_first = False
            else:
                process_input += ", "
                inputs += ", "
            if "TreeNode" in str(v.annotation):
                exists = True
                add_lib = "from python.object_libs import list_to_tree"
                if "List[" in str(v.annotation):
                    process_input += "nums_arr"
                    remain += "        roots = [list_to_tree(nums) for nums in nums_arr]\n"
                    inputs += "roots"
                else:
                    process_input += f"nums{idx}"
                    remain += f"        root{idx} = list_to_tree(nums{idx})\n"
                    inputs += f"root{idx}"
                    idx += 1
            elif "ListNode" in str(v.annotation):
                exists = True
                add_lib = "from python.object_libs import list_to_linked_list"
                if "List[" in str(v.annotation):
                    process_input += "nums_arr"
                    remain += f"        heads = [list_to_linked_list(nums) for nums in nums_arr]\n"
                    inputs += "heads"
                else:
                    process_input += f"nums{idx}"
                    remain += f"        head{idx} = list_to_linked_list(nums{idx})\n"
                    inputs += f"head{idx}"
                    idx += 1
            elif "Node" in str(v.annotation) and "Node" in cs_map and "neighbors" in cs_map["Node"][0][1]:
                # special handle Neighbour Nodes
                exists = True
                add_lib = "from python.object_libs import list_relation_to_node_neigh"
                if "List[" in str(v.annotation):
                    process_input += "nums_arr"
                    remain += f"        roots = [list_relation_to_node_neigh(nums) for nums in nums_arr]\n"
                    inputs += "roots"
                else:
                    process_input += f"nums{idx}"
                    remain += f"        node{idx} = list_relation_to_node_neigh(nums{idx})\n"
                    inputs += f"node{idx}"
            else:
                process_input += v.name
                inputs += v.name
                idx += 1

        if len(parameters) > 0:
            process_input += " = test_input\n"

        if "TreeNode" in str(return_anno):
            add_lib += ", tree_to_list" if exists else "from python.object_libs import tree_to_list"
            if "List[" in str(return_anno):
                remain += ("        res = self.{}({})\n        return [tree_to_list(root) for root in res]"
                           .format(func_name, inputs))
            else:
                remain += ("        res = self.{}({})\n        return tree_to_list(res)"
                           .format(func_name, inputs))
        elif "ListNode" in str(return_anno):
            add_lib += ", linked_list_to_list" if exists else \
                "from python.object_libs import linked_list_to_list"
            if "List[" in str(return_anno):
                remain += ("res = self.{}({})\n        return [linked_list_to_list(head) for head in "
                           "res]").format(func_name, inputs)
            else:
                remain += ("        res = self.{}({})\n        return linked_list_to_list(res)"
                           .format(func_name, inputs))
        elif "Node" in str(return_anno) and "Node" in cs_map and "neighbors" in cs_map["Node"][0][1]:
            # special handle Neighbour Nodes
            add_lib += ", node_neigh_to_list_relation" if exists else \
                "from python.object_libs import node_neigh_to_list_relation"
            if "List[" in str(return_anno):
                remain += ("        res = self.{}({})\n"
                           "        return [node_neigh_to_list_relation(root) for root in res]"
                           .format(func_name, inputs))
            else:
                remain += ("        res = self.{}({})\n        return node_neigh_to_list_relation(res)"
                           .format(func_name, inputs))
        else:
            if not modify_in_place:
                remain += "        return self.{}({})".format(func_name, inputs)
            else:
                remain += "        self.{}({})\n        return {}".format(func_name, inputs, inputs)
        import_libs.append(add_lib + "\n")

        process_input += remain
        return process_input

    @staticmethod
    def __extract_object_process_input_from_method(class_name, method):
        parameters = method[1]
        par_map = dict()
        process_input = "ops, inputs = test_input\n"
        remain = ""
        inputs = ""
        is_first = True
        idx = 0
        for v in parameters.values():
            if v.name == "self":
                continue
            if v.name == "args":
                continue
            if v.name == "kwargs":
                continue
            par_map[v.name] = v.annotation
            if is_first:
                is_first = False
                process_input += "        "
            else:
                process_input += ", "
                inputs += ", "
            if "TreeNode" in str(v.annotation):
                if "List[" in str(v.annotation):
                    process_input += "nums_arr"
                    remain += "        roots = [list_to_tree(nums) for nums in nums_arr]\n"
                    inputs += "roots"
                else:
                    process_input += f"nums{idx}"
                    remain += f"        root{idx} = list_to_tree(nums{idx})\n"
                    inputs += f"root{idx}"
                    idx += 1
            elif "ListNode" in str(v.annotation):
                if "List[" in str(v.annotation):
                    process_input += "nums_arr"
                    remain += f"        heads = [list_to_linked_list(nums) for nums in nums_arr]\n"
                    inputs += "heads"
                else:
                    process_input += f"nums{idx}"
                    remain += f"        head{idx} = list_to_linked_list(nums{idx})\n"
                    inputs += f"head{idx}"
                    idx += 1
            else:
                process_input += v.name
                inputs += v.name
                idx += 1

        if len(par_map) > 0:
            process_input += " = ops[0]\n"

        process_input += remain + f"        obj = {class_name}({inputs})\n"
        return process_input

    @staticmethod
    def __finalize_solution_code_with_single_class(cs_map, modify_in_place: bool = False):
        process_input = "pass"
        import_libs = []
        if "Solution" in cs_map:
            methods = cs_map["Solution"]
            if len(methods) == 1:
                parameters, return_anno = methods[0][1], methods[0][2]
                count = Python3Writer.__calculate_parameters(parameters)
                if count > 1:
                    init_params = "*test_input"
                elif count == 1:
                    init_params = "test_input"
                else:
                    init_params = ""
                if not modify_in_place:
                    process_input = "return self.{}({})".format(methods[0][0], init_params)
                else:
                    process_input = "self.{}({})\n        return {}".format(methods[0][0], init_params, init_params)
        else:
            class_name, methods = "", []
            for k, v in cs_map.items():
                class_name, methods = k, v
            import_libs.append("from python.object_libs import call_method\n")
            init_params = ""
            for method in methods:
                if method[0] == "__init__":
                    parameters, return_anno = methods[0][1], methods[0][2]
                    count = Python3Writer.__calculate_parameters(parameters)
                    if count > 0:
                        init_params = "*inputs[0]"
                    break

            process_input = (("ops, inputs = test_input\n        obj = {}({})\n        return [None] + "
                              "[call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]")
                             .format(class_name, init_params))
        return import_libs, process_input

    @staticmethod
    def __finalize_solution_code_complex(cs_map, modify_in_place: bool = False):
        process_input = "pass"
        import_libs = []
        if "Solution" in cs_map:
            methods = cs_map["Solution"]
            if len(methods) == 1:
                process_input = Python3Writer.__extract_process_input_from_method(
                    cs_map, modify_in_place, import_libs, methods[0])
        else:
            import_libs.append("from python.object_libs import call_method")
            if "TreeNode" in cs_map:
                import_libs.append(", list_to_tree")
                cs_map.pop("TreeNode")
            elif "ListNode" in cs_map:
                import_libs.append(", list_to_linked_list")
                cs_map.pop("ListNode")
            else:
                # Too complex to fix here
                pass
            import_libs.append("\n")
            if len(cs_map) == 1:
                class_name, methods = "", []
                for k, v in cs_map.items():
                    class_name, methods = k, v
                for method in methods:
                    if method[0] == "__init__":
                        process_input = Python3Writer.__extract_object_process_input_from_method(class_name, method)
                        break

                process_input += ("        return [None] + [call_method(obj, op, *ipt)"
                                  " for op, ipt in zip(ops[1:], inputs[1:])]")

        return import_libs, process_input

    @staticmethod
    def __write_solution_python_backup(code: str):
        strip_code = []
        define_class = []
        if '"""' in code:
            sp = code.split('"""')
            code_source = ""
            for i in range(1, len(sp), 2):
                define_class.append(sp[i])
            for i in range(0, len(sp), 2):
                code_source += sp[i]
            for line in code_source.split("\n"):
                if line.startswith("from typing import"):
                    continue
                if line.startswith("class Solution"):
                    continue
                if len(line) > 0:
                    strip_code.append(line)
        elif "class Solution" in code or "# class" in code:
            start = False
            strip_start = False
            for line in code.split("\n"):
                if line.startswith("from typing import"):
                    continue
                if line.startswith("# class"):
                    start = True
                if line.startswith("#"):
                    if start:
                        define_class.append(line[2:])
                    else:
                        if not strip_start:
                            define_class.append(line)
                        else:
                            strip_code.append(line)
                    strip_start = False
                else:
                    if strip_start:
                        strip_code.append(line)
                    if line.startswith("class Solution"):
                        strip_start = True
                    start = False
        return SOLUTION_TEMPLATE_PYTHON.format(
            "\n\n" + "\n".join(define_class) + "\n" if define_class else "",
            "pass",
            "\n".join(strip_code) if strip_code else code
        )
