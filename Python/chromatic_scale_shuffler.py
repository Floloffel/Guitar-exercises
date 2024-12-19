'''
Chromatic scale shuffler for random chromatic guitar exercise.
'''

import random
import numpy as np

# variables
zahlen = [1, 2, 3, 4]
strokes = ["Downstroke", "Upstroke"]
first_fret = np.linspace(0, 15, num=16)

# shuffling
random.shuffle(zahlen)
random.shuffle(strokes)
random.shuffle(first_fret)

# print shuffled lists
print("Chromatic Scale Exercise")
print("Finger set:", zahlen)
print(f"Start with: {strokes[0]}")
print("Index finger on fret:", int(first_fret[0]))

# keep window open until input
input("\nPress ENTER to close")

# build .exe with:
#pyinstaller --onefile chromatic_scale_shuffler.py