#controller.py
from mpm import config
from mpm.logging_ import logger
from mpm.config import Rhythm

import mpm.scales as scales
from mpm.notes import Notes
import mpm.exercise_maker as exercise_maker
import mpm.playback as playback

def set_exercise_list_midi_nums():

	def exercise_list_all_notes():
		exercise_list_all_notes = []
		for measure in config.exercise_list:
			for chunk in measure:
				for note in chunk:
					exercise_list_all_notes.append(note)
		return exercise_list_all_notes
	
	exercise_list_all_notes = exercise_list_all_notes()
	
	config.exercise_list_midi_nums = [config.scale_object.midi_nums[note] for note in exercise_list_all_notes]

	'''for note in exercise_list_all_notes:
		config.exercise_list_midi_nums.append(config.scale_object.midi_nums[note])'''

def build_scale_obj():
	config.scale_object = scales.__getattribute__(config.scaletype)(config.root)
	config.scale = config.scale_object.scale
	config.ranged_scale = config.scale_object.ranged_scale

def run():
	build_scale_obj()
	config.exercise_list = exercise_maker.run()
	set_exercise_list_midi_nums()
	playback.play()




## GETTERS AND SETTERS
# Time
def set_tempo(tempo):
	if tempo == "":
		config.tempo = 120
	else:
		config.tempo = int(tempo)

def set_beats(beats):
	if beats == "":
		config.beats = 4
	else:
		config.beats = int(beats)

def set_beat_type(beat_type):
	config.beat_type = beat_type

#Scales

def get_scaletype_list():
	scaletype_list = [i for i in (scales.__dir__()) if "__" not in i]
	return scaletype_list

def get_key_signatures():
	return ["C major"]

def set_key_signature(key_signature):
	config.key_signature = key_signature

def get_roots():
	return Notes().allnotes

def set_root(root):
	config.root = root
	logger.info("Controller::Set_Root::root = {}".format(root))

def set_flats_or_sharps(selection):
	flats = ["C","F","Bb","Eb","Ab","Db","Gb"]
	if selection in flats:
		config.flats = True
	else:
		config.flats = False

def set_scaletype(scaletype):
	if scaletype:
		config.scaletype = scaletype
	else:
		config.scaletype = "Major"

def set_startnote(startnote):
	config.startnote = startnote + config.range_start

# Pattern/Rhythm
def set_pattern(pattern):
	if pattern == "":
		config.pattern = "1"
	else:
		pattern_list = [int(num) for num in list(pattern)]
		config.pattern = pattern_list

def get_rhythms():
	return Rhythm.rhythms

def set_a_rhythm(a_rhythm):
	config.a_rhythm = a_rhythm

# Direction
def set_measure_direction(measure_direction):
	config.directions["measure"] = measure_direction
def set_exercise_direction(exercise_direction):
	config.directions["exercise"] = exercise_direction

# Grid
def set_grid(grid_selection):
	config.grid = grid_selection

def set_b_pattern(b_pattern):
	config.b_pattern = b_pattern

def set_b_rhythm(b_rhythm):
	config.b_rhythm = b_rhythm

def set_grid_scale_motion(selection):
	config.grid_scale_motion = selection

def set_title(title):
	config.title = title

# Default values
def set_default_values():
	# Time
	config.tempo = 120
	config.beats = 4
	config.beat_type = 4
	# Scale/Key
	config.range = 8
	config.key_signature = "C major"
	config.root = "C"
	config.flats = True
	config.scaletype = "Major"
	config.startnote = "C3"
	config.range_start = "3"
	config.clef = "treble"
	# Pattern/Rhythm
	config.pattern = [1,2,3,4]
	config.a_rhythm = "sixteenth"
	# Directions
	config.directions = {"measure": "up","exercise": "up"}
	# Grid
	config.grid = False
	config.b_pattern = None
	config.b_rhythm = None
	config.grid_scale_motion = None
	config.title = "Default Title"
'''
def log_config():
	# create log for all config attributes
	for i in config.__dir__():
		if "__" in i:
			pass
		else:
			logger.info('config.{}: {}'.format(i, config.__getattribute__(i)))'''