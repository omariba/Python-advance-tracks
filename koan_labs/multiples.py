def multiple_sum():
	li = []
	for i in range(1000):
		if i%3 == 0 or i%5 == 0:
			li.append(i)
			summ = 0
			for n in li:
				summ += n
	return summ
multiple_sum()