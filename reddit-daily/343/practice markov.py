import random


def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('\n\n', ' ')
    return contents

def write_file(filename, message):
    with open(filename, 'w') as file:
        file.write(message)

def build_chain(text, chain = {}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1

    return chain

def generate_message(chain, count = 100):
    word1 = random.choice(list(chain.keys()))

    message = word1.capitalize()

    while(len(message.split(' ')) < count):
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2

    return message

file = read_file('MarkovText')
chain = build_chain(file)
message = generate_message(chain)
write_file('output', message)


