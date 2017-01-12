def largest_prime_factor(args):
	i = 2
	while i*i<=args:
		if args%i:
			i+=1
		else:
			args//=i
	return args
largest_prime_factor(17)