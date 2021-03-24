from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 4], Output=False))
        self.testcases.append(case(Input=[3, 1, 4, 2], Output=True))
        self.testcases.append(case(Input=[-1, 3, 2, 0], Output=True))
        self.testcases.append(case(Input=[2, 4, 1, 3], Output=True))
        self.testcases.append(case(Input=[3, 2, 1, 4], Output=False))
        self.testcases.append(case(Input=[1, 4, 0, 4], Output=False))

    def get_testcases(self):
        return self.testcases
