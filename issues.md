# ISSUES

## C-Indexing
See notes.py for a concrete example of this issue.

The primary issue with applying range numbers to a musical scale is 
the 'C-indexed' nature of scales.  Octaves begin on C not on A, so 
we wind up with issues like this:

Cmajor scale:
[C0, D0, E0, F0, G0, A0, B0]

Aminor Scale
[A-1, B-1, C0, D0, E0, F0, G0]

This means that at certain times we need to know wether our starting note is bellow 
C or above it - this could likely be solved with some clever Exceptions and error handling.
But for now I've chosen the ugly, blunt approach of storing all our ranged notes in notes.py


## Key Signatures
SCAMP does NOT currently support key signatures.  
See the issue <a href="https://scampsters.marcevanstein.com/t/key-signature">here</a>.  This is
obviously a semi-big problem for the future of my app, and most likely means a different type of 
XML generation module will be required.

I've added an older version of xmlwriter.py to my github from an early mpm prototype.
It uses <a href="https://lxml.de/">LXML</a> to custom print our MusicXMl files and will be integrated to replace
SCAMP in the next update.

## Set default title 
Work in progress: the title should update automatically as the exercise is modified - but it should also be 
open to modification by the user in the title input form

## Grid Functionality
Restore grid functionality

## Scale/Exercise Direction
Restore 'both' directionality to measurea and exercise
Restore 'down' directionality to exercise

## Final Note
Restore 'final note' functionality to playback
