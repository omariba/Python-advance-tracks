def compounded_principal(time):

	incr_p = 0.08/1
	bracks = 1 + incr_p
	up = 1*time
	inn = bracks ** up
	A = 10000 * inn
	return int(A)

compounded_principal(30)