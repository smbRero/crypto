import sys
sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)

# return (g, x, y) a*x + b*y = gcd(x, y)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    '''modular inverce'''
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def nod(a, b):
    return egcd(a, b)[0]

def rsa_secret_key_gen(p,q,E):
    '''returns d from your prime numbers p,q and E
    E:nod(E,(p-1)(q-1)=1'''
    if not nod(E,(p-1)*(q-1) == 0):
           return -1
    return mulinv(E,(p-1)*(q-1)) % (p*q)

def rsa_crypt(message,E,N):
    return pow(message,E,N)

def rsa_decrypt(message,d,N):
    return pow(message,d,N)
	
def check_prime_root(g,p):
	'''g - кандидат в первообразный корень, p - число'''
	for l in range(1,p-1):
		if pow(g,l,p) == 1:
			return False
	if pow(g,p-1,p)==1:
			return True
	else:
			return False
			
def find_prime_root_for_prime(p):
	for g in range(2,p):
		if check_prime_root(g,p):
			return g
	return 0

def elgamal_key_gen(p,g,x):
	'''p - случайное простое число,g - первообразный корень p, x - случайное число от 1 до p-1'''
	y = pow(g,x,p)
	return y
	
def elgamal_crypt(message,p,g,y,k):
	a = pow(g,k,p)
	b = pow(y,k)*message % p
	return a,b
	
def elgamal_decrypt(a,b,x,p):
	message = b*pow(a,p-1-x) % p
	return message