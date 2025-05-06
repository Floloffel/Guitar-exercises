"""
This small trainer tells you a note value and string.
You could either play the note, the chord or the scale.
"""

import keyboard
import random

iterations = 5
notes = ["A", "Bb", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

task = ["minor", "major", "minor7", "major7", "pentatonic"]

print("press space to start and continue")

for i in range(iterations):
    keyboard.wait("space")
    print("-------------")
    note = random.choice(notes)
    string = random.randint(1, 6)
    task_choice = random.choice(task)
    print(f"String: {string}")
    print(f"Note: {note}")
    print(f"Play the {task_choice} scale")
    print("\n")