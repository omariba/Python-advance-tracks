import string

vowel = ['a','e','i','o','u']

def capitalize_first_char(sentence):
	return sentence.title()

def get_longest_word(sentence):
	if sentence == '':
		pass
	else:
		execp = string.punctuation
		for i in sentence:
			if i in execp:
				sentence = sentence.replace(i,'')
		word = sentence.split()
		li = []
		for i in word:
			li.append(len(i))
		large = max(li)
		temp = []
		for p in word:
			if len(p) == large:
				temp.append(p)
		return temp[0]
def change_letters(sentence):
	sent = []
	sent1 = []
	nom = string.ascii_lowercase
	rev = nom[1:] + nom[:1]
	punc = string.punctuation
	num = str(range(10))
	for i in sentence:
		if i == " ":
			sent.append(" ")
		elif i in punc or i in num:
			sent.append(i)
		else:
			pos = nom.index(i)
			sent.append(rev[pos])
	for n in sent:
		if n in vowel:
			n = n.swapcase()
		sent1.append(n)
	sent1 = ''.join(sent1)
	return sent1
def change_letters_with_any_key(sentence, key):
	sent = []
	sent1 = []
	nom = string.ascii_lowercase
	rev = nom[key:] + nom[:key]
	punc = string.punctuation
	num = str(range(10))
	for i in sentence:
		if i == " ":
			sent.append(" ")
		elif i in punc or i in num:
			sent.append(i)
		else:
			pos = nom.index(i)
			sent.append(rev[pos])
	for n in sent:
		if n in vowel:
			n = n.swapcase()
		sent1.append(n)
	sent1 = ''.join(sent1)
	return sent1

change_letters_with_any_key("hello world!!",3)


