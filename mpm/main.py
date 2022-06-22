#main.py 
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty
from kivy.core.window import Window

import mpm.controller as controller

Window.maximize()

#### Modules
class Module(BoxLayout):
    pass
class Panel(BoxLayout):
    pass
class Time(Module):
	def tempo(self, tempo):
		controller.set_tempo(tempo)
	def beats(self, beats):
		controller.set_beats(beats)
	def beat_type(self, beat_type):
		controller.set_beat_type(beat_type)

class ScaleModule(Module):
	def key_signature(self, key_signature):
		controller.set_key_signature(key_signature)
	def root(self, root):
		controller.set_root(root)
	def flats_or_sharps(self, selection):
		controller.set_flats_or_sharps(selection)
	def scaletype(self, scaletype):
		controller.set_scaletype(scaletype)
	def startnote(self, startnote):
		controller.set_startnote(startnote)

class Pattern(Module):
	def pattern(self, pattern):
		controller.set_pattern(pattern)
	def a_rhythm(self, a_rhythm):
		controller.set_a_rhythm(a_rhythm)

class Direction(Module):
	def measure_direction(self, measure_direction):
		controller.set_measure_direction(measure_direction)
	def exercise_direction(self, exercise_direction):
		controller.set_exercise_direction(exercise_direction)

class Grid(Module):
	def grid(self, grid_selection):
		controller.set_grid(grid_selection)
	def b_pattern(self, b_pattern):
		controller.set_b_pattern(b_pattern)
	def b_rhythm(self, b_rhythm):
		controller.set_b_rhythm(b_rhythm)
	def grid_scale_motion(self, selection):
		controller.set_grid_scale_motion(selection)

class Title(Module):
	def title(self, title):
		controller.set_title(title)

#### Menus
class RootList(Spinner):
	rootlist = controller.get_roots()
class KeySignatures(Spinner):
	key_signatures = controller.get_key_signatures()
class RhythmList(Spinner):
	rhythmlist = controller.get_rhythms()
class ScaleTypeList(Spinner):
	scaletype_list = controller.get_scaletype_list()


#### Main App Window
class MainLayout(BoxLayout):
	def __init__(self, **kwargs):
		super(MainLayout, self).__init__(**kwargs)
		Window.bind(on_key_down = self._on_keyboard_down)

	def run(self):
		# Generating Exercise Lists #TODO
		controller.run()

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
