from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 2, 3, 4], [100, 2, 7, 10]], Output=19))
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], [1, 5, 3, 4, 6]], Output=15))
		self.testcases.append(case(Input=[[4, 3, 2, 1], [33, 20, 19, 87]], Output=-1))

	def get_testcases(self):
		return self.testcases
