from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 3, 3, 2], [[0, 1], [1, 2], [1, 3]]], Output=[-1, 0, 0, 1]))
		self.testcases.append(case(Input=[[5, 6, 10, 2, 3, 6, 15], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]], Output=[-1, 0, -1, 0, 0, 0, -1]))

	def get_testcases(self):
		return self.testcases
