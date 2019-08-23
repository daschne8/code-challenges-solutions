def is_prime(number):
    for i in range(2,int((number)/2)):
        if number % i == 0:
            return False
    return True


print(is_prime(104729))

prime_array = [2]
curr_num = 2


while(True):
    curr_num += 1
    if(is_prime(curr_num)):
        prime_array.append(curr_num)
        print(curr_num)

    if len(prime_array) == 10002:
        print(prime_array[-1])
        break

