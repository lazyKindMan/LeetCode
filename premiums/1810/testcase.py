from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[2, 3], [1, 1]], 0, 1, 1, 0], Output=2))
		self.testcases.append(case(Input=[[[0, 3, 1], [3, 4, 2], [1, 2, 0]], 2, 0, 0, 2], Output=9))
		self.testcases.append(case(Input=[[[1, 0], [0, 1]], 0, 0, 1, 1], Output=-1))

	def get_testcases(self):
		return self.testcases
