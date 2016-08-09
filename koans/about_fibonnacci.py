from runner.koan import *
from koan_labs.fibonnacci import*

class AboutFibonnacci(Koan):
	def test_fibonnacci(self):
		"""
		The Fibonacci Sequence is computed based on the following formula:


		f(n)=0 if n=0
		f(n)=1 if n=1
		f(n)=f(n-1)+f(n-2) if n>1

		Please write a program using list comprehension to print the Fibonacci Sequence in comma separated
		form with a given n input.

		Example:
		If the following n is given as input to the program:

		7

		Then, the output of the program should be the first 7 Fibonnacci numbers:

		0,1,1,2,3,5,8,13


		Hints:
		We can define recursive function in Python.(You do not have to)
		Use list comprehension to generate a list from an existing list.
		Use string.join() to join a list of strings.

		"""

		self.assertEqual(fibonacci(7), 0,1,1,2,3,5,8,13, ", Expected output is 0,1,1,2,3,5,8,13")