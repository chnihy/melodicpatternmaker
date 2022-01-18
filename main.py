#! python3 

#### =========================================== ####
# 				Melodic Pattern Maker       		#
#													#
#	The main kivy app, Updates all of the config 	#
#	variables and runs the  program.				#
#													#
#### =========================================== ####

# TODO Remove Duplicates option
# TODO Key Signature
# TODO Odd Time/ Beattype == 8
# TODO Multiple Scales
# TODO Filename customization
# TODO Custom Range

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty
from kivy.core.window import Window

import melodic_pattern_maker as mpm
import playback
import config
import chords
import scales
from chords import roots
from rhythm import rhythms

from pprint import pprint as pp

Window.maximize()

#### Modules
class Module(BoxLayout):
    pass

class Panel(BoxLayout):
    pass


class Time(Module):
	def set_tempo(self, tempo):
		if tempo == "":
			config.tempo = 120
		else:
			config.tempo = int(tempo)
	
	def set_beats(self, beats):
		if beats == "":
			config.beats = 4
		else:
			config.beats = int(beats)


	def set_beattype(self, beattype):
		config.beattype = beattype


class ScaleModule(Module):
	def set_key_signature(self, key_signature):
		config.key_signature = key_signature
		print(f"config.key_signature: {config.key_signature}")
	
	def set_root(self, root):
		config.root = root
		print(f"config.root: {config.root}")

	def set_flats_or_sharps(self, selection):
		flats = ["C","F","Bb","Eb","Ab","Db","Gb"]
		if selection in flats:
			config.flats = True
		else:
			config.flats = False

	def set_scaletype(self, scaletype):
		config.scaletype = scaletype

	def set_startnote(self, startnote):
		config.startnote = startnote
		print(f"config.startnote {config.startnote}")


class Pattern(Module):
	def set_pattern(self, pattern):
		if pattern == "":
			config.pattern = "1"
		else:
			config.pattern = pattern

	def set_a_rhythm(self, a_rhythm):
		config.a_rhythm = a_rhythm


class Direction(Module):
	def set_measure_direction(self, measure_direction):
		config.measure_direction = measure_direction

	def set_exercise_direction(self, exercise_direction):
		config.exercise_direction = exercise_direction


class Grid(Module):
	def set_grid(self, grid_selection):
		config.grid = grid_selection
	
	def set_b_pattern(self, b_pattern):
		config.b_pattern = b_pattern

	def set_b_rhythm(self, b_rhythm):
		config.b_rhythm = b_rhythm

	def set_grid_scale_motion(self, selection):
		config.grid_scale_motion = selection
	

class Title(Module):
	def set_title(self, title):
		config.title = title
	

#### Menus
class RootList(Spinner):
	rootlist = roots

class KeySignatures(Spinner):
	key_signatures = scales.key_signatures

class RhythmList(Spinner):
	rhythmlist = rhythms

class ScaleList(Spinner):
	scalelist = list(scales.allscales.keys())


#### Main App Window
class MainLayout(BoxLayout):
	def __init__(self, **kwargs):
		super(MainLayout, self).__init__(**kwargs)

		# Enter key functionality binding
		Window.bind(on_key_down = self._on_keyboard_down)
	
	def config_clear(self):
		config.exercise_list = []
		config.exercise_list_2 = []
		config.combined_exercise_list = []

	def run(self):

		# Generating Exercise Lists #TODO config kwargs
		mpm.exercise_maker(beats = config.beats,
					root = config.root,
					scaletype = config.scaletype,
					flats = config.flats,
					startnote = config.startnote + "4", 
					pattern = config.pattern,
					a_rhythm = config.a_rhythm,
					measure_direction = config.measure_direction, 
					exercise_direction = config.exercise_direction, 
					grid = config.grid, 
					b_rhythm = config.b_rhythm,
					b_pattern = config.b_pattern, 
					grid_scale_motion = config.grid_scale_motion,
					pattern_scale_relation = "", 
					multi_scale = False)
		
		print("main.py ---> config.exercise_list:")
		pp(config.exercise_list)

		# Transcribe and playback
		playback.play()

	# Enter key function
	def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
		if keycode == 40:
			self.run()

#################
class MainApp(App):
	def build(self):
		
		self.title = "Melodic Pattern Maker App"

		return MainLayout()

if __name__ == "__main__":
	MainApp().run()
