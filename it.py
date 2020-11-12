def geometric( a0, an, c ) :
	i = a0
	while ( i < an ) :
		yield i
		i = i * c

def divisors( n ) :
	for i in range( 2, n+1 ) :
		k = i
		for j in range( 1, n // i+1) :
			if ( n % k == 0 ) :
				yield i
				k = k * i

def filter( sel, other ) :
	for i in other :
		if sel( i ) is True :
			yield i

def permutations( n ) :
	if n == 0 :
		yield []
	else :
		for i in permutations( n - 1 ) :
			for j in range( n ):
				i. append( j )
				yield i
				i. pop()