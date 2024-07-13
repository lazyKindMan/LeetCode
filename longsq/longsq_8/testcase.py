from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="42", Output=42))
		self.testcases.append(case(Input="   -042", Output=-42))
		self.testcases.append(case(Input="1337c0d3", Output=1337))
		self.testcases.append(case(Input="0-1", Output=0))
		self.testcases.append(case(Input="words and 987", Output=0))

	def get_testcases(self):
		return self.testcases
