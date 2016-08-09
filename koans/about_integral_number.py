from runner.koan import *
from koan_labs.integral_number import*

class AboutIntegralNumber(Koan):
	def test_integral_number(self):
		"""
		With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
		such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
		Suppose the following input is supplied to the program:
		8
		{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

		Hints:
		Consider use dict()
		"""

		self.assertEqual(integral_number(8), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64},
		 "Expected dictionary ids {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}")
