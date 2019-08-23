import math

def is_prime(number):
    number = abs(number)
    for i in range(2,int((number)**.5)+1):
        if number % i == 0:
            return False
    return True

def quad_primes(number, a, b):
    prime = number ** 2 + a*number + b
    return prime

def primes_till(a,b):
    primes = []
    i = 0
    while is_prime(quad_primes(i,a,b)) :
        primes.append(quad_primes(i,a,b))
        i += 1
    return primes


def largest_prime_sequence():
    #length, a , b
    largest_sequence = [0,0,0]
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            primes = primes_till(a,b)
            if len(primes) > largest_sequence[0]:
                largest_sequence[0] = len(primes)
                largest_sequence[1] = a
                largest_sequence[2] = b
            print(a,b,primes)
    return largest_sequence, largest_sequence[1] * largest_sequence[2]

#print(primes_till(-61,971), len(primes_till(-61,971)))
print(largest_prime_sequence())
#([71, -61, 971], -59231)