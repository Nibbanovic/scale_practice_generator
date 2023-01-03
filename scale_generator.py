from colored import fg as foreground, bg as background, attr
import random

SCALE_NAME_FORMULAS = {
    "Ionian": "wwhwwwh",
    "Dorian": "whwwwhw",
    "Phrygian": "hwwwhww",
    "Aeolian": "whwwhww",
    "Lydian": "wwwhwwh",
}

def get_key_from_value(my_dict, value):
    return list(my_dict.keys())[
        list(my_dict.values()).index(value)
    ]

CHROMATIC_WITH_SYMBOL = {
    'A': 'circle #fcbd27',
    'a': 'square #89489a',
    'B': 'circle #aad04a',
    'C': 'square #dd2a51',
    'c': 'circle #00ac99',
    'D': 'square #f78932',
    'd': 'circle #426bb0',
    'E': 'square #f4de22',
    'F': 'circle #ae2c8f',
    'f': 'square #42b956',
    'G': 'circle #f25730',
    'g': 'square #009dd9',
}
CHROMATIC = list(CHROMATIC_WITH_SYMBOL.keys())
COLORS = list(CHROMATIC_WITH_SYMBOL.values())

NATURAL_NOTES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', ]
ACCIDENTALS = ['#', 'b', '']


class Scale:
    def __init__(self, scale_name="random"):  # e.g. "C# Ionian"

        if scale_name == "random":
            self.natural_note = random.choice(NATURAL_NOTES)
            self.accidental = random.choice(ACCIDENTALS)
            self.scale_formula = random.choice(list(SCALE_NAME_FORMULAS.values()))
            self.scale_name = (self.natural_note
                               + self.accidental
                               + ' '
                               + get_key_from_value(SCALE_NAME_FORMULAS, self.scale_formula))
        else:
            (self.natural_note,
             self.accidental,
             self.scale_formula) = self.parse_scale_name(scale_name)
            self.scale_name = scale_name

        natural_note_index = self.locate_in_chromatic(self.natural_note, self.accidental)
        natural_notes_rearranged = self.rearrange_natural_notes(starting_from=self.natural_note)
        self.chromatic_indices = self.find_indices_in_chromatic(starting_from=natural_note_index,
                                                                scale_formula=self.scale_formula)

        self.scale_notes = self.get_scale_notes(natural_notes_rearranged, self.chromatic_indices)

    def print_scale(self):
        for note, chromatic_index in zip(self.scale_notes, self.chromatic_indices):
            symbol, style = self.get_symbol_and_style(chromatic_index)

            self.print_with_style(' ', style)
            self.print_with_style(note, style)
            self.print_with_style(symbol, style)
            self.print_with_style(' ', style)

        print('\n')

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

    @staticmethod
    def print_with_style(text, style):
        reset = attr("reset")
        print(style + text + reset, end='')

    @staticmethod
    def get_symbol_and_style(chromatic_index):
        note_style = COLORS[chromatic_index % len(COLORS)]
        shape, color = note_style.split()

        style = foreground(color) + background('white') + attr('bold')
        symbol = ('\u25A0' if shape == "square" else
                  '\u25CF' if shape == "circle" else
                  '??')

        return symbol, style


while True:
    test_scale = Scale()
    print(test_scale.scale_name)
    test_scale.print_scale()
    input("> ")


