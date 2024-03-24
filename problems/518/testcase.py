from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [1, 2, 5]], Output=4))
		self.testcases.append(case(Input=[3, [2]], Output=0))
		self.testcases.append(case(Input=[10, [10]], Output=1))

	def get_testcases(self):
		return self.testcases
