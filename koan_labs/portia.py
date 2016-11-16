import math

def calculate_wealth(yearnow):
	incr_p = 0.05/1
	bracks = 1 + incr_p
	up = yearnow*1
	inn = bracks ** up
	A = 1 * inn
	#A=P(1+r/n)^nt
	#t = year(s)
	#n = no of times its compounded per year
	return math.floor(A)

def find_year():
    # Your code here
    return 

calculate_wealth(100)