from runner.koan import *
from koan_labs.more_string_practice import*

class AboutMoreStringPractice(Koan):
	def test_isVowel(self):
		"""
		This is an exercise for you to gain more practice with manipulating strings
		and general control flow of a program.
		_________
		ACTIVITY:
		_________

		Go to koan_labs/more_string_practice.py.
		The method is_vowel takes in a character and returns True if the character is
		a vowel and False if the character is not a vowel. However, for this
		exercise, we will assume that y is a vowel.So if the character is y,return
		True. All other characters are non-vowels and hence should return False.

		HINT:
		VOWELS INCLUDE: AEIOUYaeiouy

		"""
		self.assertEqual(is_vowel('a'),True,"a is vowel")
		self.assertEqual(is_vowel('Y'),True,"Remember that y was a vowel")
		self.assertEqual(is_vowel('2'),False,"2 is a non-Vowel")
		self.assertEqual(is_vowel('&'),False,"& is a non-Vowel")
		self.assertEqual(is_vowel('E'),True,"This is a vowel")





	def test_positionOfFirstVowel(self):

		"""
		This is intended to helps you practice indexing in strings.
		________
		ACTIVITY:
		________

		Go to koan_labs/more_string_practice.py.
		The method position_of_first_vowel takes in a word and returns the index position of the first
		vowel in the word. If there is no vowel in the word, return -1.

		There's a catch though. If the letter y happens to be the first letter in the
		word (i.e. index 0), it shouldn't be counted as a vowel and hence you shouldn't
		return 0. However, if it occurs anywhere else, it should be the first vowel, therefore return it's
		index position. E.g, in the letter Yam, the first vowel is at index 1, i.e. a,
		but in the word rhythm, the first vowel is at index 2, i.e y

		"""
		self.assertEqual(position_of_first_vowel("yesterday"),1,"For the word 'yesterday' the postion should be 1. Try again")
		self.assertEqual(position_of_first_vowel("strength"),3,"Postion should be 3, try again")
		self.assertEqual(position_of_first_vowel("cheese"),2,"Postion should be 2, try again")
		self.assertEqual(position_of_first_vowel("dnrzs"),-1,"no vowel here mate")




	def test_Pigify(self):

		"""
		This is now where all the magic happens. We are going to  'pigify' some words.
		Pigify is just a word I made up to mean that we will transform some words based on some
		rules that I made up.
		Again, this is intended to give you more practice with strings, looping and indexing.
		________
		ACTIVITY:
		________

		Go to koan_labs/more_string_practice.py.
		The pigify function will receive a string as a parameter, and then transform the
		word based on the rules below. The function will then return the transformed word.

		You will then return the transformed string. The rules of transformation
		are as follows:

		1. If a word begins with 'a', 'e', 'i', 'o', or 'u',
		then append the string "-way" to the string and then return this transformed string.
		The arrow denotes transformation:

		Examples:

				anchor---->anchor-way
				oasis---->oasis-way
				umbrella--->umbrella-way


		2. If a word begins with a non-vowel (we will call this a consonant, but it could be a number, punctuation, or something else),
		move the prefix before the first vowel to the end with "ay" appended. Use a hyphen and treat 'y' as a vowel.
		If 'y' is the first letter of a word it should be considered a non-vowel:



				yesterday--->esterday-yay
				strength----->ength-stray
				rhythm-------->ythm-rhay

		3. Words that begin with a 'qu' should be treated as though the 'u' is a consonant.


				quiz--->iz-quay
				queue--->eue-quay
				quay----->ay-quay


		4. If a word contains no vowels it should be treated as though it starts with a vowel.
		For example :

		"zzz" will be translated to "zzz-way".

		"""
		self.assertEqual(pigify("boy"),"oy-bay","Pigify me better man")
		self.assertEqual(pigify("coy"),"oy-cay","Pigify me better man")
		self.assertEqual(pigify("brutal"),"utal-bray","Pigify me better man")
		self.assertEqual(pigify("quay"),"ay-quay","Pigify me better man")
		self.assertEqual(pigify("bbb"),"bbb-way","Pigify me better man")
		self.assertEqual(pigify("yellow"),"ellow-yay","Pigify me better man")
