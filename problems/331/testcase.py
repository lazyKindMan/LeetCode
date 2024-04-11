from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="9,3,4,#,#,1,#,#,2,#,6,#,#", Output=True))
		self.testcases.append(case(Input="1,#", Output=False))
		self.testcases.append(case(Input="9,#,#,1", Output=False))
		self.testcases.append(case(Input="#,#,3,5,#", Output=False))

	def get_testcases(self):
		return self.testcases
