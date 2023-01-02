SCALE_NAME_FORMULAS = {
    "Ionian": "wwhwwwh",
    "Dorian": "whwwwhw",
    "Phrygian": "hwwwhww",
    "Aeolian": "whwwhww",
    "Lydian": "wwwhwwh",
}

NATURAL_NOTES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', ]
# samo kad ispisujemo skalu

CHROMATIC = ['A', 'a', 'B', 'C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g']


# da skužimo koje se note koriste

def print_scale(scale_name):  # e.g. "C# Ionian"

    natural_note, accidental, scale_formula = parse_scale_name(scale_name)

    natural_note_index = locate_in_chromatic(natural_note, accidental)
    natural_notes_rearranged = rearrange_natural_notes(starting_from=natural_note)
    chromatic_indices = find_indices_in_chromatic(starting_from=natural_note_index,
                                                  scale_formula=scale_formula)  # scale number as the machine sees it

    return get_scale_notes(natural_notes_rearranged, chromatic_indices)


def parse_scale_name(scale_name):
    '''returns the root, its accidental and the scale formula'''
    natural_note_and_accidental, scale_type = scale_name.split()
    accidental = ('' if len(natural_note_and_accidental) < 2
                  else natural_note_and_accidental[1])

    natural_note = natural_note_and_accidental[0]
    scale_formula = SCALE_NAME_FORMULAS[scale_type]

    return natural_note, accidental, scale_formula


def locate_in_chromatic(natural_note, accidental):
    return CHROMATIC.index(natural_note) + (1 if accidental == '#'
                                            else -1 if accidental == 'b'
    else 0)


def rearrange_natural_notes(starting_from):
    starting_index = NATURAL_NOTES.index(starting_from)
    base_notes_rearranged = NATURAL_NOTES[starting_index:] + NATURAL_NOTES[:starting_index]
    return base_notes_rearranged


def find_indices_in_chromatic(starting_from, scale_formula):
    '''generates notes in machine form from root note and scale formula'''
    output = []
    for step in scale_formula:
        output.append(starting_from)
        starting_from = (starting_from
                         + (2 if step == 'w' else 1)
                         )
    return output


def get_scale_notes(natural_notes_rearranged, chromatic_indices):
    scale_notes = []
    starting_natural_note_chromatic_index = CHROMATIC.index(natural_notes_rearranged[0])
    for natural_note, chromatic_index in zip(natural_notes_rearranged, chromatic_indices):
        accidentals = infer_accidentals(natural_note, chromatic_index,
                                        starting_natural_note_chromatic_index)
        scale_notes.append(natural_note + accidentals)
    return scale_notes


def infer_accidentals(natural_note, chromatic_index, starting_natural_note_chromatic_index):
    natural_note_chromatic_index = CHROMATIC.index(natural_note)
    if is_new_octave(natural_note_chromatic_index, starting_natural_note_chromatic_index):
        natural_note_chromatic_index += len(CHROMATIC)

    signed_num_accidentals = chromatic_index - natural_note_chromatic_index
    accidental = ('#' if signed_num_accidentals > 0 else
                  'b' if signed_num_accidentals < 0 else
                  '')
    return abs(signed_num_accidentals) * accidental


def is_new_octave(natural_note_chromatic_index, starting_natural_note_chromatic_index):
    return natural_note_chromatic_index < starting_natural_note_chromatic_index


print(print_scale("Db Phrygian"))
