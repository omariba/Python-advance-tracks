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
	for i in vowel:
		if word.startswith(i):
			if i == "Y" or i == "y":
				word = word[1:] + '-' + word[:1] + 'ay'
				return word
			else:
				return word + "-way"
	for q in word:
		if q in vowel:
			if word.startswith('Q') or word.startswith('q'):
				word = word[2:] + '-' + word[:2] + 'ay'
				return word
			elif word.index(q) != 0:
				n = word.index(q)
				word = word[n:] + '-' + word[:n] + 'ay'
				return word
	for i in word:
		if i not in vowel:
			return word + "-way"
			
print pigify("queue")