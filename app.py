#!/usr/bin/python
import random
scales = [
    "Whole tone",
    "Diminished"
]

keys = [
    "Ab", "A", "A#",
    "Bb", "B",
    "C", "C#",
    "Db", "D", "D#",
    "Eb", "E",
    "F", "F#",
    "Gb", "G", "G#"
]

print(random.choice(keys) + " - " + random.choice(scales))
