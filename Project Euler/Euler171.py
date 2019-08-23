__author__ = 'dasch_000'
import math

def sum_square(number):
    number = str(number)
    sumation = 0
    for i in number:
        sumation += int(i)**2
    return sumation

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

for n in range(0,10**20):
    sum_of_all = 0
    n_list = []
    if is_square(sum_square(n)):
        sum_of_all += n
        n_list.append(n)
    print(n)
print(sum_of_all)
