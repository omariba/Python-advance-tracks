import string
def password_integrity(args):
	validator = {""}
	if len(args) not in range(6,13):
		return False
	elif " " in args:
		return False
	else:
		for i in string.lowercase:
			if i in args:
				validator.add("a")
		for i in string.uppercase:
			if i in args:
				validator.add("A")
		for i in string.punctuation:
			if i in args:
				validator.add("!")
		for i in str(range(10)):
			if i in args:
				validator.add("1")
		if len(validator) < 5:
			return False
		else:
			return True
	
print password_integrity("a F1'*'")

# 				if i not in string.uppercase:
# 					if i not in string.punctuation:
# 						if i not in str(range(10)):
# 							return False
# validator.add(i)
# continue
# import string
# def punc(arg):
# 	if arg in string.punctuation:
# 		return True
# 	else:
# 		return False
		# for i in args:
		# 	if i in string.lowercase:
		# 		for s in validator:
		# 			if s.islower() == False:
		# 				validator.add(i)
		# 	elif i in string.uppercase:
		# 		for s in validator:
		# 			if s.isupper() == False:
		# 				validator.add(i)
		# 	elif i in string.punctuation:
		# 		for s in validator:
		# 			if punc(s) == False:
		# 				validator.add(i)
		# 	elif i in str(range(10)):
		# 		for s in validator:
		# 			if s.isdigit() == False:
		# 				validator.add(i)