# MelodicPatternMaker
#### The Melodic Pattern Maker (mpm for short) is part of a suite of apps for music education.  
Built using Scamp and Kivy, it exports to XML files in LilyPond or MuseScore/Sibelius/Finale formats.

<img src="/images/preview.png">
<img src="/images/preview2.png">


MelodicPatternMaker creates scale pattern exercises based of a wide range of user input:
  * Key
  * Scale
  * Root
  * Rhythm
  * Pattern (ex 1234)

It also supports creating rhythmic grids to help work on combining subdivisions. There are a lot of possibilities with all of the various modifiers! GRIDS ARE NOT CURRENTLY FUNCTIONAL, will be again soon!

## How to install and run
### Clone Repo
```bash
git clone https://github.com/chnihy/melodicpatternmaker.git
cd melodicpatternmaker
```
### Install Requirements
```bash
pip3 install -r requirements.txt
```
### Launch app.py
```bash
python3 app.py
```

## Project Design
The biggest change in the refactor is converting the entire project to an MVC architecture.

While changes will be made, and more structure will be added in the future, the general divisions
can be considered as follows.

### The Model:
config.py, notes.py, scales.py

### The View:
main.py, main.ky

### The Controller:
controller.py, playback.py

```
.
├── README.md
├── app.py
├── file.log
├── issues.md
├── mpm
│   ├── __init__.py
│   ├── config.py
│   ├── controller.py
│   ├── exercise_maker.py
│   ├── logging_.py
│   ├── main.kv
│   ├── main.py
│   ├── notes.py
│   ├── playback.py
│   └── scales.py
└── requirements.txt
```

## Todo
- [ ] Add testing
- [ ] Prettier UI
- [ ] Support for more scales including modes, altered, diminsihed etc...
- [ ] Support for odd time signatures
- [ ] Support for multiple scales in one exercise
- [ ] Interactive playback/integrated midi display
- [ ] Add grid support - Currently disabled 


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


