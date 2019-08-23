def digit_fifth_powers(power):
    sum_list = []
    theoretical_min = 2**power
    theoretical_max = 9**power * power
    for i in range(theoretical_min, theoretical_max +1):
        num = str(i)
        sum_num = 0
        for digit in num:
            sum_num += int(digit)**power

        if sum_num == i:
            sum_list.append(i)
    return sum_list

print(sum(digit_fifth_powers(5)))
#443839