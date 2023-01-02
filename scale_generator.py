from colored import fg, bg, attr

scale_name_formulas = {
    "Ionian": "wwhwwwh",
    "Dorian": "whwwwhw",
    "Phrygian": "hwwwhww",
    "Aeolian": "whwwhww",
    "Lydian": "wwwhwwh",
}

base_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G',]
# samo kad ispisujemo skalu

notes = ['A', 'a', 'B', 'C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g']
# da skužimo koje se note koriste

def parse_scale_name(scale_name):
    '''returns the root, its accidental and the scale formula'''
    root_and_accidental, scale_type = scale_name.split()
    accidental = ('' if len(root_and_accidental) < 2
                  else root_and_accidental[1])

    root = root_and_accidental[0]
    scale_formula = scale_name_formulas[scale_type]

    return root, accidental, scale_formula

def generate_notes(scale_formula, note_index):
    '''generates notes in machine form from root note and scale formula'''
    output = []
    for step in scale_formula:
        output.append(note_index)
        note_index = (note_index
                      + (2 if step == 'w' else 1)
                      )
    return output

def spell_scale(scale_name):    # e.g. "C# Ionian"

    root, accidental, scale_formula = parse_scale_name(scale_name)

    root_index = notes.index(root) + (1 if accidental == '#'
                                      else -1 if accidental == 'b'
                                      else 0)
    base_root_index = base_notes.index(root)

    base_notes_rearranged = base_notes[base_root_index:] + base_notes[:base_root_index]
    machine_scale = generate_notes(scale_formula, root_index)       # scale number as the machine sees it

    spelled_scale = []
    for base_note, machine_note_index in zip(base_notes_rearranged, machine_scale):

        notes_index = notes.index(base_note)
        if notes_index < notes.index(base_notes_rearranged[0]):
            notes_index += len(notes)

        num_accidentals = machine_note_index - notes_index

        spelled_scale.append(base_note + abs(num_accidentals)*('#' if num_accidentals > 0 else
                                                               'b' if num_accidentals < 0 else
                                                               ''))
    return spelled_scale


print(spell_scale("Db Phrygian"))










