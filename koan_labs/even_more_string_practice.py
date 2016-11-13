def capitalize_first_char(sentence):
	return sentence.title()

def get_longest_word(sentence):
	a = 0
	b = 1
	c = 1
	word = sentence.split()
	while c <= 5:
		 print max(word[a],word[b])
		 c +=1
		 a=b
		 b=c
def change_letters(sentence):
	# Your code here
	return

def change_letters_with_any_key(sentence, key):
	# Your code here
	return 

get_longest_word("nelson mandela is an elegant person")