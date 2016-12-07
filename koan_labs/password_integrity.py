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
	
print password_integrity("ABd1234@1")
