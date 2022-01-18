# melodicpatternmaker
The Melodic Pattern Maker is part of a suite of apps for music education.  
Built using Scamp and Kivy - it exports to XML files in LilyPond or MuseScore/Sibelius/Finale formats

Melodic Pattern Maker (mpm) creates scale pattern exercises based of a wide range of user input:
  - Key
  - Scale
  - Root
  - Rhythm
  - Pattern (ex 1234)

It also supports creating rhythmic grids to help work on combining subdivisions. There are a lot of possibilities with all of the various modifiers!

# Some future planned updates:
  - Prettier UI
  - Support for more scales including modes, altered, diminsihed etc...
  - Support for odd time signatures
  - Support for multiple scales in one exercise
  - Interactive playback/integrated midi display

# Requirements:
- Requires install of Kivy and Scamp, as well as their dependecies
- Both are included in the venv, to run mpm from the venv, cd to mpm directory and enter
   $ source ./mpm_venv/bin/activate
- To install requirements yourself:
- pip3 install kivy
- pip3 install scamp
- pip3 install abjad
- brew install lilypond

# How to Install and Run Melodic Pattern Maker
1. Download as zip
2. cd to download directory
3. Install requirements or activate venv (see Requirements)
4. $ python3 main.py
