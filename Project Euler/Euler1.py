multiples = set()
for number in range(0,1000):
    if number % 3 == 0 or number % 5 == 0:
        multiples.add(number)

total = 0
for number in multiples:
    total += number
print(multiples)
print(total)