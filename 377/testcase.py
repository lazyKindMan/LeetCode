from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3], 4), Output=7))
        self.testcases.append(case(Input=([9], 3), Output=0))
        self.testcases.append(case(Input=([4, 2, 1], 32), Output=39882198))

    def get_testcases(self):
        return self.testcases
