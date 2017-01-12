from runner.koan import *
from koan_labs.password_integrity import*

class AboutPasswords(Koan):
	def test_password_integrity(self):
		"""
		A website requires the users to input username and password to register. Write a program to check the 
		validity of any password provided.
		Following are the criteria for checking the password:
		1. At least 1 letter between [a-z]
		2. At least 1 number between [0-9]
		1. At least 1 letter between [A-Z]
		3. At least 1 character from [$#@]
		4. Minimum length of transaction password: 6
		5. Maximum length of transaction password: 12
		Your program should accept a string password and will check according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
		Example
		If the following passwords are given as input to the program:
		ABd1234@1
		Then, the output of the program should be:
		True

		"""

		self.assertEqual(password_integrity("ABd1234@1"), True, "Password meets requirements")
		self.assertEqual(password_integrity("a F1'*'"), False, "Password does not meet requirements")
		self.assertEqual(password_integrity("2w3E*"), False, "Password does not meet requirements")
		self.assertEqual(password_integrity("2We3345"), False, "Password does not meet requirements")
