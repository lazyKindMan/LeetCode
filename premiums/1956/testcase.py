from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 1], [6, 1]], 2], Output=3))
		self.testcases.append(case(Input=[[[3, 3], [1, 2], [9, 2]], 2], Output=2))
		self.testcases.append(case(Input=[[[3, 3], [1, 2], [9, 2]], 3], Output=4))

	def get_testcases(self):
		return self.testcases
