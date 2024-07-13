from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=3749, Output="MMMDCCXLIX"))
		self.testcases.append(case(Input=58, Output="LVIII"))
		self.testcases.append(case(Input=1994, Output="MCMXCIV"))

	def get_testcases(self):
		return self.testcases
