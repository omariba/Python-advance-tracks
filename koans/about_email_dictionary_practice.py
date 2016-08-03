from runner.koan import *
from koan_labs.email_dictionary_practice import *

class AboutEmailDictionaryPractice(Koan):
	"""docstring for AboutEmailDictionaryPractice"""
	def test_email_dictionary_practice(self):
		"""
		This exercise is intended to give you more pracice with dictionaries.
		Have fun with this one.

		You are given a list of strings of course information, where each string is in the format 
		"coursename:person:email". Your task is to determine the course with the most people and to return the emails of those people in the largest course. 
		The emails should be returned as a string with the emails in alphabetical order. 
		If there is more than one largest course, return the emails of such course that comes first in alphabetical order.
		For example, assume the course information list is:

		CompSci 100:Fred Jack Smith:fjs@duke.edu
		History 117:Fred Jack Smith:fjs@duke.edu
		CompSci 102:Arielle Marie Johnson:amj@duke.edu
		CompSci 100:Arielle Marie Johnson:amj@duke.edu
		CompSci 006:Bertha White:bw@duke.edu
		Econ 051:Bertha White:bw@duke.edu
		English 112:Harry Potter:hp@duke.edu
		CompSci 100:Harry Potter:hp@duke.edu


		CompSci 100 is the largest course with three people. The string returned would be "amj@duke.edu fjs@duke.edu hp@duke.edu"

Course information is represented as a string with the course listed ":" separator, then a name, then a ":" separator and then an email address.

Given a list of courses (a list of strings), return the emails in alphabetical order and separated by a blank for the course with the largest enrollment.

			
		"""
		self.assertEqual(["CompSci 100:Fred Jack Smith:fjs@duke.edu", "Art 100:Bella F Hotfield:bfh4@duke.edu"],"bfh4@duke.edu","Try Harder")
		
		self.assertEqual(["CompSci 100:Fred Jack Smith:fjs@duke.edu"],"fjs@duke.edu","Try Harder")

		self.assertEqual(["CompSci 100:Fred Jack Smith:fjs@duke.edu", 
  "History 117:Fred Jack Smith:fjs@duke.edu", 
  "CompSci 102:Arielle Marie Johnson:amj@duke.edu", 
  "CompSci 100:Arielle Marie Johnson:amj@duke.edu", 
  "CompSci 006:Bertha White:bw@duke.edu",
  "Econ 051:Bertha White:bw@duke.edu", 
  "English 112:Harry Potter:hp@duke.edu",
  "CompSci 100:Harry Potter:hp@duke.edu"],"amj@duke.edu fjs@duke.edu hp@duke.edu","Try Harder")

		
		
