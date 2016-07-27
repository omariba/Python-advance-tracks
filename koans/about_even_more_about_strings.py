from runner.koan import *
from koan_labs.even_more_string_practice import*

class AboutEvenMoreStringPractice(Koan):
	def test_capitalizeFirstChar(self):
		"""
			__________
			ACTIVITY 1
			__________
			Go to koan_labs/even_more_string_practice.py.
			Given a sentence, the method capitalize_first_char should return the sentence with first letters of all words
			capitalized.
		"""
		#self.assertEqual(capitalize_first_char("did you write the test scripts"), "Did You Write The Test Scripts")
		#self.assertEqual(capitalize_first_char("who are you"), "Who Are You")

	def test_getLongestWord(self):
		"""
			__________
			ACTIVITY 2
			__________
			Go to koan_labs/even_more_string_practice.py.
			In method get_longest_word, return the largest word of the given sentence. 
			If there are two or more words that are the same length, return the first word from the string with 
			that length. Ignore punctuation and assume the sentence will not be an empty string.

		"""
		#self.assertEqual(get_longest_word("where are you"), "where")
		#self.assertEqual(get_longest_word("a beautiful sentence^&!"), "beautiful")
		#self.assertEqual(get_longest_word("a confusing /:sentence:/[ this is not!!!!!!!~"), "confusing")



	def test_changeLetters(self):
		"""
		Practice even more with strings.
		__________
		ACTIVITY 3
		__________
		Go to koan_labs/even_more_string_practice.py. 
		Taking a sentence an argument, method change_letters should modify the sentence in the following ways. 
		- Replace all alphabetical letters in the sentence with the one that follows it. Don't replace special 
		  characters. 
		- Then capitalize all the vowels of the modified sentence.
		- Remember z's next letter is a

			Example: 
				The sentence    "hello world!!" 
				should become   "Ifmmp xpsmE!!"

				The sentence    "where did you come from"
				should become   "xIfsf EjE zpv dpnf gspn"

		Return the modified string.
		Hint:
		This is a modification of the Caesar cipher with a key of 1
		"""

		#self.assertEqual(change_letters("where did you come from"), "xIfsf EjE zpv dpnf gspn")
		#self.assertEqual(change_letters("where!! did.. you,, !!come!! from1111"), "xIfsf!! EjE.. zpv,, !!dpnf!! gspn1111")
		#self.assertEqual(change_letters("zootopia"), "AppUpqjb")

	def test_changeLettersWithAnyKey(self):
		"""
		Practice even more with strings.
		__________
		ACTIVITY  4
		__________
		This a modification of the previous activity.
		Go to koan_labs/even_more_string_practice.py.

		Taking a sentence and a key (any integer) as arguments, method change_letters_with_any_key should modify 
		the sentence in the following ways. 
		- Replace all alphabetical letters in the sentence depending with the key given. Don't replace special 
		  characters. 
		- Should work with both negative and positive ints. Negative integers encrypy in reverse.
		- Then capitalize all the vowels of the modified sentence.
		- Remember to loop back to a after z

			Example: 
				The sentence    "hello world!!" with a key of 3 
				should become   "khOOr zrUOg!!"

				The sentence    "hello world!!" with a key of -3
				should become   "EbIIl tlOIA!!"

		Return the modified string.
		Hint:
		This is a modification of the Caesar cipher that works with any key.
		ASCII and modulus will take you a long way.
		"""

		self.assertEqual(change_letters_with_any_key("hello world!!",3), "khOOr zrUOg!!")
		self.assertEqual(change_letters_with_any_key("hello world!!",-3), "EbIIl tlOIA!!")

