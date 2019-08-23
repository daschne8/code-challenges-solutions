def is_prime(xy):
    da_number = int((xy+1)/2)
    for i in range(2,da_number):
        if xy%i == 0:
            return False

    return True

test_number = 600851475143
high_range = int(600851475143/500)

for div_number in range(high_range,0,-1):
    #print("current ",div_number)
    if test_number%div_number == 0:
        if is_prime(div_number):
            print(div_number)
            break

print("Warblgarbl")
