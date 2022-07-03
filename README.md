# MelodicPatternMaker
#### The Melodic Pattern Maker (mpm for short) is part of a suite of apps for music education.  
Built using Scamp and Kivy, it exports to XML files in LilyPond or MuseScore/Sibelius/Finale formats.

Work in progress - see <a href="./ISSUES.md">Issues</a>

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

## Project Design
The biggest change in the refactor is converting the entire project to an MVC architecture.

While changes will be made, and more structure will be added in the future, the general divisions
can be considered as follows.

### The Model:
config.py, notes.py, scales.py

### The View:
main.py, main.ky

### The Controller:
controller.py, playback.py, exercise_maker.py

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
│   ├── view.kv
│   ├── view.py
│   ├── notes.py
│   ├── transcribe.py
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
see <a href="./ISSUES.md">Issues</a>


