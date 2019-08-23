def is_prime(number):
    for i in range(2,int((number)**.5)+1):
        if number % i == 0:
            return False
    return True

def circular_check(prime_array, number):
    primes = [number]
    for i in range(0,len(number)):
        if number[i:] + number[0:i] not in prime_array:
            return None
        else:
            primes.append(number[i:] + number[0:i])
    return set(primes)


def find_circular_primes(limit):
    primes_list = []
    for i in range(11, limit):
        if is_prime(i):
            primes_list.append(str(i))

    circular_primes = [str(2),str(3),str(5),str(7)]
    for prime in primes_list:
        primes = circular_check(primes_list,prime)
        print(primes)
        if primes is not None:
            for number in primes:
                circular_primes.append(number)
                primes_list.remove(number)
    return circular_primes



circ_primes = find_circular_primes(100)
print(len(circ_primes))
print(circ_primes)


#why won't 3 and 7 show up?
#55