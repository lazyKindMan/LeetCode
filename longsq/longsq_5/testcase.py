from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="babad", Output="bab"))
		self.testcases.append(case(Input="cbbd", Output="bb"))

	def get_testcases(self):
		return self.testcases
