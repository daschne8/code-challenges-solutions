import random


def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read().split('\n')
    notes = []
    for note in contents:
        note = note.split(' ')
        note[1] = 0
        notes.append(note)

    return notes

def write_file(filename, message):
    with open(filename, 'w') as file:
        file.write(message)

def build_chain(text, chain = {}):
    notes = text

    index = 1
    for note in notes[index:]:
        key = notes[index - 1][0]
        if key in chain:
            chain[key].append(note)
        else:
            chain[key] = [note]
        index += 1

    return chain

def generate_song(chain, count = 100):
    note_1 = random.choice(chain[random.choice(list(chain.keys()))])

    song = note_1[0] + ' ' + str(0) + ' ' + note_1[2]
    time = 0
    while(len(song.split('\n')) < count):
        note_2 = random.choice(chain[note_1[0]])
        time += float(note_1[2])
        note_1 = note_2
        song += '\n' + note_2[0] + ' ' + str(time) + ' ' + note_2[2]

    return song

file = read_file('ProceduralMusicInput')
chain = build_chain(file)
song = generate_song(chain)
write_file('output', song)

'''
file = read_file('ProceduralMusicInput')
chain = build_chain(file)
song = generate_song(chain)
write_file('output', song)
'''