from pynput import keyboard
from notes import aNote, aSharp, bNote, cNote, cSharp, dNote, dSharp, eNote, fNote, fSharp, gNote, gSharp, aNote
go = 1

def on_press(key):
    if key.char == "a":
        aNote(go)
    if key.char == "s":
        aSharp(go)
    if key.char == "d":
        bNote(go)
    if key.char == "f":
        cNote(go)
    if key.char == "g":
        cSharp(go)
    if key.char == "h":
        dNote(go)
    if key.char == "j":
        dSharp(go)
    if key.char == "k":
        eNote(go)
    if key.char == "l":
        fNote(go)
    if key.char == ";":
        fSharp(go)
    if key.char == "'":
        gNote(go)
    if key.char == "z":
        gSharp(go)

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
