def triangular_number(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    return sum

def get_factors(number):
    factors = []
    range_num = int(number**.5)
    for i in range(range_num,0,-1):
        if number % i == 0:
            factors.append(i)
            if int(number/i) not in factors:
                factors.append(int(number/i))
    return factors


def first_to_500_divisors():
    i = 0
    triangle_num = 0
    while(True):
        i += 1
        triangle_num = triangular_number(i)
        #print("i: {}, Triangle Number {}".format(i,triangle_num))
        if len(get_factors(triangle_num)) > 500:
            return triangle_num


print(first_to_500_divisors())
#76576500
