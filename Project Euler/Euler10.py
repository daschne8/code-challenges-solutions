def is_prime(number):
    for i in range(2,int((number)**.5)+1):
        if number % i == 0:
            return False
    return True

def prime_sum_method(number):
    prime_sum = 0
    for i in range(2,number):
        if is_prime(i):
            prime_sum += i
            print(i)
    return prime_sum

print(prime_sum_method(2000000))
#142913828922