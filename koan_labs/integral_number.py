def integral_number(args):
	dic = dict()
	for i in range(1,args+1):
		if dic.has_key(i) == False:
			dic[i] = i**2
	return dic

integral_number(8)