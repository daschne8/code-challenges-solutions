def is_palindrome(pot_palin):
    if len(pot_palin) == 0:
        return False

    for i in range(int(len(pot_palin)/2)+1):
        if pot_palin[i-1] != pot_palin[-i]:
            return False
    return True

def binary_converter(number):
    #find highest x for 2**x then go down from there
    #checking each iteration

    if number == 0 or number < 0:
        return ''
    if number == 1:
        return '0'
    if number == 2:
        return '1'

    highest_value = 0
    binary_string = '1'
    prospective_number = 0
    while 2**highest_value <= number:
        highest_value += 1

    highest_value -= 1
    prospective_number += 2**highest_value

    for x in range(highest_value-1,-1,-1):
        if prospective_number + 2**x > number:
            binary_string = binary_string + '0'
        else:
            binary_string = binary_string +'1'
            prospective_number += 2**x

    return binary_string


def double_base_palindromes(limit):
    sum = 0
    double_base_array = []
    for x in range(limit):
        if is_palindrome(str(x)) and is_palindrome(binary_converter(x)):
            sum += x
            double_base_array.append(x)
    return sum, double_base_array


test1, test2 = double_base_palindromes(1000000)
print(test1)
print(test2)
#2 doesn't count?
#872187





