from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=123, Output=321))
		self.testcases.append(case(Input=-123, Output=-321))
		self.testcases.append(case(Input=120, Output=21))

	def get_testcases(self):
		return self.testcases
