from pynput import keyboard
from notes import aNote, aSharp, bNote, cNote, cSharp, dNote, dSharp, eNote, fNote, fSharp, gNote, gSharp, aNote


def on_press(key):
    if key.char == "a":
        aNote()
    if key.char == "s":
        aSharp()
    if key.char == "d":
        bNote()
    if key.char == "f":
        cNote()
    if key.char == "g":
        cSharp()
    if key.char == "h":
        dNote()
    if key.char == "j":
        dSharp()
    if key.char == "k":
        eNote()
    if key.char == "l":
        fNote()
    if key.char == ";":
        fSharp()
    if key.char == "'":
        gNote()
    if key.char == "z":
        gSharp()

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# ...or, in a non-blocking fashion:
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
