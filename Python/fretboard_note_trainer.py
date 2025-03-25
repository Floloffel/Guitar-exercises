import random
import time
import keyboard
import colorama as cr

# Initialize colorama (needed for Windows)
cr.init(autoreset=False)

iterations = 20

# Define the notes in an octave
notes = ["A", "Bb", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

# Define the open string notes for a standard tuned guitar
open_strings = ["E", "A", "D", "G", "B", "E"][::-1]


# Function to get the note at a specific fret and string
def get_note_at(fret, string):
    open_note = open_strings[string - 1]
    open_note_index = notes.index(open_note)
    note_index = (open_note_index + fret) % len(notes)
    return notes[note_index]


print(f"Starting {iterations} iterations")
print(
    f"Press {cr.Style.BRIGHT}{cr.Fore.YELLOW}Esc{cr.Style.RESET_ALL} or {cr.Style.BRIGHT}{cr.Fore.YELLOW}Enter{cr.Style.RESET_ALL} to exit early"
)
print(
    f"Press {cr.Style.BRIGHT}{cr.Fore.YELLOW}spacebar{cr.Style.RESET_ALL} to reveal the note"
)
print("-------------")


time_start = time.time()
i = 0
while i < iterations:
    # Toggle colors for variety
    if i % 2 == 0:
        color = cr.Fore.YELLOW
    else:
        color = cr.Fore.GREEN

    fret = random.randint(0, 24)
    string = random.randint(1, 6)
    note = get_note_at(fret, string)

    print(f"{color}String: {string}")
    print(f"Fret: {fret}")

    # Wait for space while also allowing Enter to quit
    cont = False
    while cont == False:
        if keyboard.is_pressed("enter") or keyboard.is_pressed("esc"):
            print("Exiting early...")
            exit()
        if keyboard.is_pressed("space"):
            time.sleep(0.3)  # Small delay to avoid multiple spacebar inputs
            cont = True

    print(f"{color}Note: {note}{cr.Style.RESET_ALL}")
    print("-------------")
    i += 1

time_needed = time.time() - time_start
print(f"Time needed: {round(time_needed, 1)} seconds")
