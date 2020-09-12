import numpy as np
import simpleaudio as sa

# modify later all frequecies for later dynamic tuning
globalNoteFrequency = 0
globalOctave = 2


def aNote(globalOctave):
    frequency = globalNoteFrequency + 440  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    # play_obj.wait_done()


def aSharp(globalOctave):
    frequency = globalNoteFrequency + 466.16  
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    # play_obj.wait_done()

def bNote(globalOctave):
    frequency =globalNoteFrequency + 493.88  
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    # play_obj.wait_done()

def cNote(globalOctave):
    frequency =globalNoteFrequency + 523.25  
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    # play_obj.wait_done()

def cSharp(globalOctave):
    frequency =globalNoteFrequency + 554.37  
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    # play_obj.wait_done()


    
def dNote(globalOctave):
    frequency =globalNoteFrequency + 587.33  
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    # play_obj.wait_done()

def dSharp(globalOctave):
    frequency =globalNoteFrequency + 622.25 
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting


def eNote(globalOctave):
    frequency =globalNoteFrequency + 659.25 
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting


def fNote(globalOctave):
    frequency = globalNoteFrequency + 698.46 
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)


def fSharp(globalOctave):
    frequency =globalNoteFrequency + 739.99 
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

def fSharp(globalOctave):
    frequency =globalNoteFrequency + 739.99 
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)



def gNote(globalOctave):
    frequency =globalNoteFrequency + 783.99 
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)


def gSharp(globalOctave):
    frequency =globalNoteFrequency + 830.61 
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * globalOctave * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    
# next octaive
# def aNote():
#     frequency = 830.61 
#     fs = 44100  # 44100 samples per second
#     seconds = 3  # Note duration of 3 seconds
#     # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
#     t = np.linspace(0, seconds, seconds * fs, False)

#     # Generate a 440 Hz sine wave
#     note = np.sin(frequency * t * globalOctave * np.pi)

#     # Ensure that highest value is in 16-bit range
#     audio = note * (2**15 - 1) / np.max(np.abs(note))
#     # Convert to 16-bit data
#     audio = audio.astype(np.int16)

#     # Start playback
#     play_obj = sa.play_buffer(audio, 1, 2, fs)