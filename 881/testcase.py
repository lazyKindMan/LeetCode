from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2], 3), Output=1))
        self.testcases.append(case(Input=([3, 2, 2, 1], 3), Output=3))
        self.testcases.append(case(Input=([3, 5, 3, 4], 5), Output=4))

    def get_testcases(self):
        return self.testcases
