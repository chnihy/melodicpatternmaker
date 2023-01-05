# MelodicPatternMaker
#### The Melodic Pattern Maker (mpm for short) is part of a suite of apps for music education.  
Built using Scamp and Kivy, it exports to XML files in LilyPond or MuseScore/Sibelius/Finale formats.

Tree
```
.
├── README.md
├── app.py
├── file.log
├── images
│   ├── preview.png
│   └── preview2.png
├── issues.md
├── mpm
│   ├── __init__.py
│   ├── config.py
│   ├── controller.py
│   ├── exercise_maker.py
│   ├── grid.py
│   ├── logging_.py
│   ├── midi.py
│   ├── notes.py
│   ├── rhythm.py
│   ├── scales.py
│   ├── transcribe.py
│   ├── view.kv
│   └── view.py
└── requirements.txt
```

See project structure in the last <a href="https://github.com/chnihy/melodicpatternmaker/pull/2">pull request</a>

<img src="/images/preview.png">
<img src="/images/preview2.png">

MelodicPatternMaker creates scale pattern exercises based of a wide range of user input:
  * Key
  * Scale
  * Root
  * Rhythm
  * Pattern (ex 1234)

~~It also supports creating rhythmic grids to help work on combining subdivisions. There are a lot of possibilities with all of the various modifiers!~~ GRIDS ARE NOT CURRENTLY FUNCTIONAL, will be again soon!

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

## Todo
- [ ] Add testing
- [ ] Prettier UI
- [ ] Support for more scales including modes, altered, diminsihed etc...
- [ ] Support for odd time signatures
- [ ] Support for multiple scales in one exercise
- [ ] Interactive playback/integrated midi display
- [ ] Add grid support - Currently disabled 


# ISSUES
see <a href="./issues.md">Issues</a>


