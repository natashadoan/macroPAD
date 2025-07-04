import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.direct import DirectPins
from kmk.keys import KC
import neopixel

# kmk setup + GPIOs
keyboard = KMKKeyboard()
keyboard.matrix = DirectPins(
    pins=(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4),
    value_when_pressed=False,
    pull=True,
)

# neopixel setup
pixels = neopixel.NeoPixel(board.GP6, 2, brightness=0.3, auto_write=True)

# one color per key
COLORS = [
    (255, 20, 147),   # hot pink:     Key 0
    (64, 224, 208),   # turquoise:    Key 1
    (255, 165, 0),    # orange:       Key 2
    (138, 43, 226),   # purple:       Key 3
    (50, 205, 50),    # bright green: Key 4
]

# key behaviors
from kmk.handlers.sequences import simple_key_sequence

def set_color_for_key(index):
    def fn(key, keyboard):
        color = COLORS[index]
        pixels[0] = color
        pixels[1] = color
    return fn

# LED triggers
keys = [
    simple_key_sequence((KC.C,), on_press=set_color_for_key(0)),  # Copy
    simple_key_sequence((KC.V,), on_press=set_color_for_key(1)),  # Paste
    simple_key_sequence((KC.X,), on_press=set_color_for_key(2)),  # Cut
    simple_key_sequence((KC.Z,), on_press=set_color_for_key(3)),  # Undo
    simple_key_sequence((KC.Y,), on_press=set_color_for_key(4)),  # Redo
]

keyboard.keymap = [keys]

if __name__ == '__main__':
    keyboard.go()
