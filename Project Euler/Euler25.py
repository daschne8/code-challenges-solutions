def gen_fib():
    i = 1
    fib_num = 1
    prev_num = 0
    while True:
        i += 1
        additive = fib_num
        fib_num += prev_num
        prev_num = additive
        if len(str(fib_num)) == 1000:
            return i, fib_num

print(gen_fib())
#4782