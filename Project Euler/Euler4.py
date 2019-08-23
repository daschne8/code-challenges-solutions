def is_pallindrome(number):
    number = str(number)
    for i in range(0,len(number)):
        if number[i] != number[-(i+1)]:
            return False
    return True


largest_palindrome = 0
for x in range(999,100,-1):
    for y in range(999,100,-1):
        xy = x * y
        if(is_pallindrome(xy) and xy > largest_palindrome):
            largest_palindrome = xy

print(largest_palindrome)