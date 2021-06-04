from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="aababbab", Output=2))
        self.testcases.append(case(Input="bbaaaaabb", Output=2))

    def get_testcases(self):
        return self.testcases
