from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="III", Output=3))
		self.testcases.append(case(Input="LVIII", Output=58))
		self.testcases.append(case(Input="MCMXCIV", Output=1994))

	def get_testcases(self):
		return self.testcases
