from colored import fg, bg, attr


note_colors = {
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


def print_with_style(text, style):
    reset = attr("reset")
    print(style + text + reset, end='')



for note in note_colors.items():
    shape, color = note[1].split()

    style = fg(color) + bg('#ffffff') + attr("bold")
    symbol = '\u25A0' if shape == "square" else '\u25CF'

    print_with_style(' ', style)
    print_with_style(note[0], style)
    print_with_style(symbol, style)
    print_with_style(' ', style)

print('\n')









