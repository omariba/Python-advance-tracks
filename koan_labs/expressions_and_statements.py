def compounded_principal(time):

	incr_p = 0.08/1
	bracks = 1 + incr_p
	up = 1*time
	inn = bracks ** up
	A = 10000 * inn
	return int(A)
	#A=P(1+r/n)^nt
	#t = year(s)
	#n = no of times its compounded per year

compounded_principal(30)