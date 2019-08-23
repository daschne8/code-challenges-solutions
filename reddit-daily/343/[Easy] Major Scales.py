def note(scale_note, solfage):
    chromatic_scale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    major_scale = [0,2,4,5,7,9,11]
    do_solfage = {'Do':0, 'Re':1, 'Mi':2, 'Fa':3, 'So':4, 'La':5, 'Ti':6}

    scale = []
    scale_shift = chromatic_scale.index(scale_note)
    for x in major_scale:
        position = (x + scale_shift)%12
        scale.append(chromatic_scale[position])

    scale_position = do_solfage[solfage]


    wanted_note = scale[scale_position]
    #print(scale)
    print(wanted_note)

note("C", "Do")
note("C", "Re")
note("C", "Mi")
note("D", "Mi")
note("A#", "Fa")