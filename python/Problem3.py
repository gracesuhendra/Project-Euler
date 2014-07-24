'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def prime(n):
    primes = []
    i = 2
    while (i<=n/i):
        while (n%i==0):
            n = n/i
            primes.append(i)
        i = i+1
    if (n>1):
        primes.append(n)
    return primes

def max_prime(p):
    return max(prime(p))
    
    
print max_prime(600851475143)
