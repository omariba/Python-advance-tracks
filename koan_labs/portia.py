import math

def calculate_wealth(yearnow):
	incr_p = 0.05/1
	bracks = 1 + incr_p
	up = yearnow*1
	inn = bracks ** up
	A = 1 * inn
	return math.floor(A)
	#A=P(1+r/n)^nt
	#t = year(s)
	#n = no of times its compounded per year

def find_year():
    wealthportia = 100000
    wealth= 1
    numberofyears= 1
    while wealth <= wealthportia:
    	wealth= 1.05* (float(wealth))
    	wealthportia = 1.04* (float(wealthportia))
    	numberofyears += 1
    return numberofyears

print find_year() 