from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[0, 1], [1, 2], [3, 4]]], Output=2))
		self.testcases.append(case(Input=[5, [[0, 1], [1, 2], [2, 3], [3, 4]]], Output=1))

	def get_testcases(self):
		return self.testcases
