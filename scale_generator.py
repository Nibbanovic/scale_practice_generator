
scale_name_formulas = {
    "Ionian": ['1', '2', '3', '4', '5', '6', '7'],
    "Dorian": ['1', '2', 'b3', '4', '5', '6', 'b7'],
    "Phrygian": ['1', 'b2', 'b3', '4', '5', 'b6', 'b7'],
    "Aeolian": ['1', '2', 'b3', '4', '5', 'b6', '7'],
}

def get_key_form_value(dict, val):
    for key, value in dict.items():
        if val in value:
            return key

    return "Key doesn't exist"


def spell_scale(scale_name):    # e.g. "C Ionian"

    notes = {
        1: 'C',
        2: ['C#', 'Db'],
        3: 'D',
        4: ['D#', 'Eb'],
        5: 'E',
        6: 'F',
        7: ['F#', 'Gb'],
        8: 'G',
        9: ['G#', 'Ab'],
        10: 'A',
        11: ['A#', 'Bb'],
        12: 'B',
    }

    root_note, scale_type = scale_name.split()
    scale_formula = scale_name_formulas[scale_type]
    accidental = ''

    if 'b' or '#' in root_note:     # scrape the accidental
        accidental = root_note[-1]

    starting_degree = (get_key_form_value(notes, root_note))

    # worry about enharmonics when placing the root note
    if accidental == '#':
        scale_spelled = notes[starting_degree][0]
    elif accidental == 'b':
        scale_spelled = notes[starting_degree][1]
    else:
        scale_spelled = notes[starting_degree]


    for interval in scale_formula:
        starting_degree +

    return scale_spelled



print(spell_scale("D# Aeolian"))











