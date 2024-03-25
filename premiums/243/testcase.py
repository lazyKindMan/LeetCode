from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice'], Output=3))
		self.testcases.append(case(Input=[['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'], Output=1))

	def get_testcases(self):
		return self.testcases
