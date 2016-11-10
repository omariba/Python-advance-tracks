def compounded_principal(time):
	p = 10000
	r = 0.08
	t = time
	n = 1

	incr_p = r/n
	bracks = 1 + incr_p
	up = n*t
	inn = bracks ** up
	A = p * inn
	return int(A)

compounded_principal(30)