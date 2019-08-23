"""Unfinished, need more efficient algorithm, can't figure out why 
convergent fraction algorythm not working"""






#x**2 - Dy**2 = 1
# y = sqr((1-x**2)/D)
#D cannot be square
#find min x value with given D
#x that isn't 1
import math

def quadratic_Diophantine(number):
    if (number**.5).is_integer():
        return 0

    x = 1
    while(True):
        x += 1
        y = ((x**2 - 1)/number)**.5
        #print(x,y)
        if (y).is_integer():
            return(x)

def convergent_fraction(number):
    if (number**.5).is_integer():
        return 0


    target = number**.5             #sqrt(D) since x/y should converge toward sqrt(D)
    x = int(target)                 #starting x
    y = 1                           #starting y
    prev_divergence = target - (x/y)  #distance from target value
    curr_divergence = abs(target - x / y)
    counter = 0
    while(x**2 + number * y**2 != 1):
        counter += 1
        if (counter == 20):
            return x

        curr_divergence = abs(target - (x / y))
        if curr_divergence <= prev_divergence:
            x += 1
        else:# prev_divergence > curr_divergence:
            y += 1
        print(x, y, prev_divergence, curr_divergence)
        prev_divergence = curr_divergence
    return x




def find_largest_x(limit):
    largest_x = 0
    for i in range(2,limit+1):
        #number = quadratic_Diophantine(i)
        number = convergent_fraction(i)
        print(i, number)
        if number > largest_x:
            largest_x = number

    return largest_x

print(convergent_fraction(7))
#print(find_largest_x(1000))
#print(quadratic_Diophantine(2))

