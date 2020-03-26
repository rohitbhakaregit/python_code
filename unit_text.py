import unittest
import cap_unit

class  test(unittest.TestCase):
	def testcase(self):
		text="Rohit"
		Result= cap_unit.capitalise(text)
		self.assertEqual(Result,"Rohit")