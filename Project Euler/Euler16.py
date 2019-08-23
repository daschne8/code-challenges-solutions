def sum_of_digits(number):
    num_array = list(str(number));
    sum = 0
    for i in num_array:
        sum += int(i)

    return sum

print(sum_of_digits(2**1000))
#1366
