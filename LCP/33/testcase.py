from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 3], [6, 8]), Output=4))
        self.testcases.append(case(Input=([9, 0, 1], [0, 2, 2]), Output=3))

    def get_testcases(self):
        return self.testcases
