import re

alph_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char_list = list(alph_string) #remember to + 1
char_value = {}

for i in range(len(alph_string)):
    char_value[alph_string[i]] =  i + 1

def import_name_list():
    name_list = []
    with open('Euler22Text', newline='\n') as inputfile:
        pre_names = inputfile.read().splitlines()
        for names in pre_names:
            name_list.append(re.findall(r"[\w]+", names))
    return sorted(name_list[0])

def name_value(name_index,name):
    name_value = 0
    for char in name:
        name_value += char_value[char]
    name_value *= name_index
    return name_value

def total_name_sum():
    sum = 0
    name_list = import_name_list()
    for i in range(len(name_list)):
        sum += name_value(i + 1, name_list[i])
    return sum








print(total_name_sum())
#871198282