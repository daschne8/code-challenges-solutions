def sum_squares(number):
    sum_total = 0
    for i in range(1,number+1):
        sum_total += i**2

    return sum_total

def square_sums(number):
    sum_total = 0
    for i in range(1, number+1):
        sum_total += i

    return sum_total**2

def difference(number):
    return square_sums(number) - sum_squares(number)

print(difference(100))