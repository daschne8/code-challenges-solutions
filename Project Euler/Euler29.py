def distint_powers(length):
    distinct_powers_list = []
    for a in range(2,length+1):
        for b in range(2,length+1):
            distinct_powers_list.append(a**b)
    distinct_powers_list = set(distinct_powers_list)
    return len(distinct_powers_list), distinct_powers_list

print(distint_powers(100))
#9183