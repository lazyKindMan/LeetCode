from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		# self.testcases.append(case(Input=[['RandomizedSet', 'insert', 'remove', 'insert', 'getRandom', 'remove', 'insert', 'getRandom'], [[], [1], [2], [2], [], [1], [2], []]], Output=[None, True, False, True, 2, True, False, 2]))
		self.testcases.append(case(Input=[["RandomizedSet","insert","insert","remove","insert","remove","getRandom"], [[],[0],[1],[0],[2],[1],[]]], Output=[None, True, True, True, True, True, 2]))

	def get_testcases(self):
		return self.testcases
