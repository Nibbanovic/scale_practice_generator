SCALE_NAME_FORMULAS = {
    "Ionian": "wwhwwwh",
    "Dorian": "whwwwhw",
    "Phrygian": "hwwwhww",
    "Aeolian": "whwwhww",
    "Lydian": "wwwhwwh",
}

NATURAL_NOTES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', ]

CHROMATIC = ['A', 'a', 'B', 'C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g']


class Scale:
    def __init__(self, scale_name):  # e.g. "C# Ionian"

        (self.natural_note,
         self.accidental,
         self.scale_formula) = self.parse_scale_name(scale_name)

        natural_note_index = self.locate_in_chromatic(self.natural_note, self.accidental)
        natural_notes_rearranged = self.rearrange_natural_notes(starting_from=self.natural_note)
        chromatic_indices = self.find_indices_in_chromatic(starting_from=natural_note_index,
                                                           scale_formula=self.scale_formula)

        self.scale_notes = self.get_scale_notes(natural_notes_rearranged, chromatic_indices)

    def print_scale(self):
        print(self.scale_notes)

    @staticmethod
    def parse_scale_name(scale_name):
        natural_note_and_accidental, scale_type = scale_name.split()

        accidental = ('' if len(natural_note_and_accidental) < 2
                      else natural_note_and_accidental[1])
        natural_note = natural_note_and_accidental[0]
        scale_formula = SCALE_NAME_FORMULAS[scale_type]

        return natural_note, accidental, scale_formula

    @staticmethod
    def locate_in_chromatic(natural_note, accidental):
        return CHROMATIC.index(natural_note) + (1 if accidental == '#'
                                                else -1 if accidental == 'b'
                                                else 0)

    @staticmethod
    def rearrange_natural_notes(starting_from):
        starting_index = NATURAL_NOTES.index(starting_from)
        base_notes_rearranged = NATURAL_NOTES[starting_index:] + NATURAL_NOTES[:starting_index]
        return base_notes_rearranged

    @staticmethod
    def find_indices_in_chromatic(starting_from, scale_formula):
        output = []
        for step in scale_formula:
            output.append(starting_from)
            starting_from = (starting_from
                             + (2 if step == 'w' else 1)
                             )
        return output

    def get_scale_notes(self, natural_notes_rearranged, chromatic_indices):
        scale_notes = []
        starting_natural_note_chromatic_index = CHROMATIC.index(natural_notes_rearranged[0])
        for natural_note, chromatic_index in zip(natural_notes_rearranged, chromatic_indices):
            accidentals = self.infer_accidentals(natural_note, chromatic_index,
                                                 starting_natural_note_chromatic_index)
            scale_notes.append(natural_note + accidentals)
        return scale_notes

    def infer_accidentals(self, natural_note, chromatic_index, starting_natural_note_chromatic_index):
        natural_note_chromatic_index = CHROMATIC.index(natural_note)
        if self.is_new_octave(natural_note_chromatic_index, starting_natural_note_chromatic_index):
            natural_note_chromatic_index += len(CHROMATIC)

        signed_num_accidentals = chromatic_index - natural_note_chromatic_index
        accidental = ('#' if signed_num_accidentals > 0 else
                      'b' if signed_num_accidentals < 0 else
                      '')
        return abs(signed_num_accidentals) * accidental

    @staticmethod
    def is_new_octave(natural_note_chromatic_index, starting_natural_note_chromatic_index):
        return natural_note_chromatic_index < starting_natural_note_chromatic_index


test_scale = Scale("Db Phrygian")
test_scale.print_scale()
print(test_scale)
print(test_scale.scale_notes)



