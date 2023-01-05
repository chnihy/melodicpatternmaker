from mpm import config
from mpm.logging_ import logger
from mpm.rhythm import Rhythm

import mpm.scales as scales
from mpm.notes import __Notes__
import mpm.exercise_maker as exercise_maker
import mpm.transcribe as transcribe

class Controller:
	def __init__(self):
		self.set_default_config_values()

	def set_exercise_list_midi_nums(self):
		exercise_list_all_notes = self.get_exercise_list_all_notes()
		config.exercise_list_midi_nums = [config.scale_object.midi_nums[note] for note in exercise_list_all_notes]

	def get_exercise_list_all_notes(self):
		exercise_list_all_notes = []
		for measure in config.exercise_list:
			for chunk in measure:
				for note in chunk:
					exercise_list_all_notes.append(note)
		return exercise_list_all_notes


	def build_scale_obj(self):
		# select scale class and assign to config
		config.scale_object = scales.__getattribute__(config.scaletype)(config.root)
		config.scale = config.scale_object.scale
		config.ranged_scale = config.scale_object.ranged_scale

	def run(self):
		self.build_scale_obj()
		config.exercise_list = exercise_maker.get_exercise_list()
		self.set_exercise_list_midi_nums()
		transcribe.run()


	## GETTERS AND SETTERS FROM VIEW
	# Time
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

	def set_beat_type(self, beat_type):
		config.beat_type = beat_type

	#Scales
	def get_scaletype_list(self):
		scaletype_list = [i for i in (scales.__dir__()) if "__" not in i]
		return scaletype_list

	def get_key_signatures(self):
		return ["C major"]

	def set_key_signature(self, key_signature):
		config.key_signature = key_signature

	def get_roots(self):
		return __Notes__.get_raw_notes("all")

	def set_root(self, root):
		config.root = root
		#logger.info("Controller::Set_Root::root = {}".format(root))

	def set_scaletype(self, scaletype):
		if scaletype:
			config.scaletype = scaletype
		else:
			config.scaletype = "Major"

	def set_startnote(self, startnote):
		config.startnote = startnote + config.range_start

	# Pattern/Rhythm
	def set_pattern(self, pattern):
		if pattern == "":
			config.pattern = "1"
		else:
			pattern_list = [int(num) for num in list(pattern)]
			config.pattern = pattern_list

	def get_rhythms(self):
		return Rhythm.get_rhythms()

	def set_a_rhythm(self, a_rhythm):
		config.a_rhythm = a_rhythm

	# Direction
	def set_measure_direction(self, measure_direction):
		config.directions["measure"] = measure_direction

	def set_exercise_direction(self, exercise_direction):
		config.directions["exercise"] = exercise_direction

	# Grid
	def set_grid(self, grid_selection):
		config.grid = grid_selection

	def set_b_pattern(self, b_pattern):
		config.b_pattern = b_pattern

	def set_b_rhythm(self, b_rhythm):
		config.b_rhythm = b_rhythm

	def set_grid_scale_motion(self, selection):
		config.grid_scale_motion = selection

	def set_title(self, title):
		config.title = title

	# Default values
	def set_default_config_values(self):
		config.tempo = 120
		config.beats = 4
		config.beat_type = 4
		config.range = 8
		config.key_signature = "C major"
		config.root = "C"
		config.flats = True
		config.scaletype = "Major"
		config.startnote = "C3"
		config.range_start = "3"
		config.clef = "treble"
		config.pattern = [1,2,3,4]
		config.a_rhythm = "sixteenth"
		config.directions = {"measure": "up","exercise": "up"}
		config.grid = False
		config.b_pattern = None
		config.b_rhythm = None
		config.grid_scale_motion = None
		config.title = "Default Title"

	def log_config(self):
		# log all config attributes
		for i in config.__dir__(self):
			if "__" in i:
				pass
			else:
				logger.info('config.{}: {}'.format(i, config.__getattribute__(i)))