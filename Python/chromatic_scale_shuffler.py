"""
Chromatic scale shuffler for random chromatic guitar exercise.
"""

import random
import numpy as np
import keyboard

# variables
numbers = [1, 2, 3, 4]
strokes = ["Downstroke", "Upstroke"]
max_starting_fret = 15
index_finger_fret = np.linspace(0, max_starting_fret, num=int(max_starting_fret + 1))

# shuffling
random.shuffle(numbers)
random.shuffle(strokes)
random.shuffle(index_finger_fret)

# print shuffled lists
print("Chromatic Scale Exercise")
print("Finger set:", numbers)
print(f"Start with: {strokes[0]}")
print("Index finger on fret:", int(index_finger_fret[0]))

print("\nPress any key to exit...")
keyboard.read_event()  # Wait for any key before closing

# build .exe with:
# pyinstaller --onefile chromatic_scale_shuffler.py
