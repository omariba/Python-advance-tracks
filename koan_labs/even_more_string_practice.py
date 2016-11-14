import string

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
	# Your code here
	return

def change_letters_with_any_key(sentence, key):
	# Your code here
	return 

get_longest_word("wewewew nelson !#@$mandela is a s$%^erene p@#$erson")
