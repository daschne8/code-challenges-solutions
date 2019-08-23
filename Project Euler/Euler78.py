
def breaker(number):
    combos = []
    for i in range(1, int(number/2)+1):
        combos.append([number-i,i])

    return combos



def coin_partitions(number_of_coins):
    cumulative_partitions = []
    partitions_list = [[number_of_coins]]
    #num_of_partitions = 1
    while len(partitions_list) > 0:
        partition = partitions_list.pop()
        #print(partition)
        for i in range(len(partition)):
            if partition[i] > 1:
                new_partitions = breaker(partition[i])
                for part in new_partitions:
                    new_list = sorted(partition[0:i] + partition[i+1:] + part)
                    partitions_list.append(new_list)
                    #num_of_partitions += 1
        cumulative_partitions.append(partition)
    new_list = []
    for i in cumulative_partitions:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(len(coin_partitions(5)))
print(coin_partitions(6))
print(len(coin_partitions(7)))
print(len(coin_partitions(8)))
'''value_found = False
i = 5
while(value_found == False):
    i += 1
    p_len = len(coin_partitions(i))
    if(p_len % 1000000 == 0):
        print(i,p_len)

'''
# p(n) = x
#p(1) = 1
#p(2) = 2
#