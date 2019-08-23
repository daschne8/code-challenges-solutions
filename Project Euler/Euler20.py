def factorial(number):
    n = 1
    for i in range(1,number+1):
        n *= i
    return n

def sum_digits(number):
    number = factorial(number)
    number = list(str(number))
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum

print(sum_digits(100))
#648