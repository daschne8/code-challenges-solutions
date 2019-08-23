def Euler_fibonacci_2():
    Sequence = [1,2]
    i=0
    while i < 4000000:
        i = Sequence[-1] + Sequence[-2]
        if i < 4000000:
            Sequence.append(i)

    total = 0
    for number in Sequence:
        if number % 2 == 0:
            total += number

    print(Sequence)
    print(total)

Euler_fibonacci_2()
