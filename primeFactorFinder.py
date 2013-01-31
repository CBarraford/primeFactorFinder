def primes():
  sieve   = []
	current = 2
	
	while True:
		isPrime = True
		
		for prime in sieve:
			if current % prime == 0:
				isPrime = False
				break
		
		if isPrime:
			yield current
			
			sieve.append(current)
				
		current = current + 1
		

def primeFactors(x, factorsList):	
	primeList	= primes()
	current		= primeList.next()
	listLength	= len(factorsList)
	
	while current <= x/2:
		if x % current == 0:
			factorsList.append(current)
			primeFactors(x/current, factorsList)
			break
			
		current	= primeList.next()
	
	if (len(factorsList) == listLength):
		factorsList.append(x)


root	= 600851475143
factors	= []

primeFactors(root, factors)
		
print factors
