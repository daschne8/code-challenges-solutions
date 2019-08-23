
def current_value(one=0,two=0,five=0,ten=0,twenty=0,fifty=0,hundred=0,two_hundred=0):
     return one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + hundred * 100 + two_hundred * 200



'''combo_num, combo_array  = coin_sums()
print(combo_num)
for row in combo_array: print(row)'''


def c_sums(goal):
    combo_array = []
    for two_hundred in range(int(goal/200)+1):
        if two_hundred * 200 == goal:
            new_combo = [0, 0, 0, 0, 0, 0, 0, two_hundred]
            combo_array.append(new_combo)
        elif two_hundred * 200 < goal:
            for hundred in range(int(goal/100)+1):
                if two_hundred * 200 + hundred * 100 == goal:
                    new_combo = [0, 0, 0, 0, 0, 0, hundred, two_hundred]
                    combo_array.append(new_combo)
                elif two_hundred * 200 + hundred * 100 < goal:
                    for fifty in range(int(goal / 50)+1):
                        if two_hundred * 200 + hundred * 100 + fifty * 50 == goal:
                            new_combo = [0, 0, 0, 0, 0, fifty, hundred, two_hundred]
                            combo_array.append(new_combo)
                        elif two_hundred * 200 + hundred * 100 + fifty * 50 < goal:
                            for twenty in range(int(goal / 20)+1):
                                if two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 == goal:
                                    new_combo = [0, 0, 0, 0, twenty, fifty, hundred, two_hundred]
                                    combo_array.append(new_combo)
                                elif two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 < goal:
                                    for ten in range(int(goal / 10)+1):
                                        if two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 + ten * 10 == goal:
                                            new_combo = [0, 0, 0, ten, twenty, fifty, hundred, two_hundred]
                                            combo_array.append(new_combo)
                                        elif two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 + ten * 10 < goal:
                                            for five in range(int(goal / 5)+1):
                                                if two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 == goal:
                                                    new_combo = [0, 0, five, ten, twenty, fifty, hundred, two_hundred]
                                                    combo_array.append(new_combo)
                                                elif two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 < goal:
                                                    for two in range(int(goal / 2)+1):
                                                        if two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 + two * 2 == goal:
                                                            new_combo = [0, two, five, ten, twenty, fifty, hundred,
                                                                         two_hundred]
                                                            combo_array.append(new_combo)
                                                        elif two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 < goal + two * 2:
                                                            for one in range(goal+1):
                                                                if two_hundred * 200 + hundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 + two * 2 + one == goal:
                                                                    new_combo = [one, two, five, ten, twenty, fifty,hundred,two_hundred]
                                                                    combo_array.append(new_combo)
                                                                    print(new_combo)
    return combo_array


combo_array = c_sums(200)
print(len(combo_array))

#73682