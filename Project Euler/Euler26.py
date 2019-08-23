from decimal import *
import math

context = Context(prec=2000)
setcontext(context)

def find_cycle(number):
    num = Decimal(1)/Decimal(number)
    num = str(num)[2:]
    halfway = int(len(num)/2)
    pattern_length = 0
    pattern = ''
    for i in range(halfway+1):
        #if it repeats the for the rest of the cycle return it
        for pat_len in range(1,halfway):
            if split_match(num[i:],pat_len) == True:
                return num[i:i+pat_len]
    return ('')


def split_match(the_string, length):
    the_array = []
    for i in range(int(len(the_string)/length)):
        the_array.append(the_string[i*length:i*length+length])
    for i in the_array:
        if i != the_array[0] or len(the_array) <= 1:
            return False
    return True

def to_1000():
    #length, number
    greatest_fraction = [0,0]
    for i in range(2,1001):
        print(i, find_cycle(i))
        length = len(find_cycle(i))
        if length > greatest_fraction[0]:
            greatest_fraction[1] = length
            greatest_fraction[0] = i
    return greatest_fraction





print(to_1000())
#983
