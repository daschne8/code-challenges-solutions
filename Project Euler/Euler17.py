num_to_word = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
               11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
               18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy",
               80:"eighty", 90:"ninety", 100:"hundred", 1000:"thousand"}

def create_num(num):
    num = str(num)
    word = ''
    length = len(num)
    if length >=1 and num[-1] != str(0):
        word = num_to_word[int(num[-1])]
    if length >= 2 and num[-2] != str(0):
        word = num_to_word[int(num[-2] + str(0))] + ' ' + word
    #overwrite teens
    if length >=2 and int(num[-2:]) in num_to_word:
        word = num_to_word[int(num[-2:])]
    #' and '
    if length >= 3 and (num[-1] != '0' or num[-2] != '0'):
        word = 'and ' + word
    if length >= 3 and (num[-3] != '0'):
        word = num_to_word[int(num[-3])] + ' ' + num_to_word[100] + ' ' + word
    if length >= 4 and num[-4] != 0:
        word = num_to_word[int(num[-4])] + ' ' + num_to_word[1000] + ' ' + word

    return word

def str_len(words):
    sum = 0
    words_array = words.split()
    for word in words_array:
        sum += len(word)
    return sum

thousand_sum = 0
for i in range (1,1001):
    thousand_sum += str_len(create_num(i))

print(thousand_sum)

#21124




