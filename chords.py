#! python3
# random chords for kivy app
# TODO Difficulty levels/dict entries
# TODO Integrate Mingus lib

import random

roots = ["A", "B", "C", "D", "E", "F", "G",
         "Ab", "Bb", "Db", "Eb", "Gb",
         "A#", "C#", "D#", "F#", "G#"]

chord_qualities = {"Easy": ["", "min", "7", ],
                    "Medium": ["7", "min7b5", "maj7", "min7", "dim", "maj6", "maj9"],
                    "Hard": ["7", "min7b5", "maj7", "min7", "dim", "maj6", "maj9", "min11", "6/9", "7b9", "7#9", "7#11", "13", "b9b5", "#9#5"]}
def randomchords(difficultyState, numOfChords):
    # returns a specified number of randomly selected chords

    chordlist = []
    rootList = []

    for num in range(int(numOfChords)):
        while True:
            randomRoot = roots[random.randint(0, (len(roots)-1))]
            rootList.append(randomRoot)

            if rootList.count(randomRoot) >= 2:
                continue
            
            else:
                break
    
        randomQuality = chord_qualities[difficultyState][random.randint(0, len(chord_qualities[difficultyState])-1)]

        randomChord = randomRoot + randomQuality

        chordlist.append(randomChord)
        
    return chordlist
    # removing the leading white space
