smallest_positive = 0
number = 1000000
number_found = False;
while(number_found == False):
    number += 1
    for i in range(2,21):
        if number % i != 0:
            break
        if i >= 16:
            print(str(i) + ', ' + str(number))
        if i == 20 and number % i == 0:
            smallest_positive = number
            number_found = True

print(smallest_positive)
#232792560
