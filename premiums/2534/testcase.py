from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, 1, 2, 4], [0, 1, 0, 0, 1]], Output=[0, 3, 1, 2, 4]))
		self.testcases.append(case(Input=[[0, 0, 0], [1, 0, 1]], Output=[0, 2, 1]))

	def get_testcases(self):
		return self.testcases
