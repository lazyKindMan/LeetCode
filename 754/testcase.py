from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=3, Output=2))
        self.testcases.append(case(Input=2, Output=3))
        self.testcases.append(case(Input=-2, Output=3))
        self.testcases.append(case(Input=100000, Output=447))
        self.testcases.append(case(Input=5, Output=5))

    def get_testcases(self):
        return self.testcases
