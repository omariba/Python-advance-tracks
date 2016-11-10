vowel = ['A','E','I','O','U','Y','a','e','i','o','u','y']
def is_Vowel(character):
	if character in vowel:
		return True
	else:
		return False
def position_of_first_vowel(word):
	for i in word:
		if i in vowel:
			if i == "Y" or i == "y":
				if word.index(i) == 0:
					continue
			else:
				return word.index(i)
	return -1

def pigify(word):
	#code goes here.
	return

position_of_first_vowel('yesterday')