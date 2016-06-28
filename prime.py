number = 2
while number <= 100:
	is_prime = True
	trial = 2
	while trial < number:
		if number % trial == 0:
			is_prime = False
		trial +=1
	if is_prime:
		print number
	number +=1