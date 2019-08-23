import math
import random

def measures_generator():
    starting_comp = []
    filepath = 'MozartStartingComposition'
    with open(filepath) as fp:
        for line in fp:
            split_line = line.split()
            starting_comp.append(split_line)

    measure_start = 0
    measures = []
    measure = []
    for line in starting_comp:

        if float(line[1]) == measure_start + 3 or line == starting_comp[-1]:
            measures.append(measure)
            measure = []
            measure_start += 3

        measure.append([line[0], float(line[1]) - measure_start, line[2]])

    return measures


def measure_selection():
    selection_field = []
    filepath = 'MeasureSelection'
    with open(filepath) as fp:
        for line in fp:
            split_line = line.split()
            selection_field.append(split_line)

    measures = []
    dice_roll = random.randint(1,6) + random.randint(1,6) - 1

    for i in range(len(selection_field)):
        measures.append(int(selection_field[i][dice_roll]))

    return measures


def song_generater():
    selected_measures = measure_selection()
    measures = measures_generator()
    composition = []
    for measure in selected_measures:
        index = selected_measures.index(measure)
        adjusted_measure = measures[measure]
        for note in adjusted_measure:
            note[1] = float(note[1]) + index * 3
        composition.append(adjusted_measure)
        #composition.append(measures[measure])

    return composition

def write_song_to_file(composition):
    filepath = 'MozartComposition'
    open(filepath,'w').close()
    with open(filepath,'w') as fp:
        for measure in composition:
            for note_description in measure:
                for description in note_description:
                    print(description)
                    fp.write(str(description) + ' ')
                fp.write('\n')


write_song_to_file(song_generater())






