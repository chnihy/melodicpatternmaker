#controller.py
from mpm import config
import mpm.scales as scales
import mpm.exercise_maker as exercise_maker
import mpm.playback
from mpm.config import Rhythm

def build_scale_obj():
	config.scale_object = scales.__getattribute__(config.scaletype)(config.root)

def run():
	build_scale_obj()
	config.exercise_list = exercise_maker.run()
	playback.play()

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
	scales_dir = list(scales.__dir__())
	scaletype_list=[]
	for i in scales_dir:
		if "__" in i:
			pass
		else:
			scaletype_list.append(i)
	return scaletype_list

def get_key_signatures():
	return scales.__Scale__("C").allnotes

def set_key_signature(key_signature):
	config.key_signature = key_signature

def get_roots():
	return scales.__Scale__("C").allnotes

def set_root(root):
	config.root = root

def set_flats_or_sharps(selection):
	flats = ["C","F","Bb","Eb","Ab","Db","Gb"]
	if selection in flats:
		config.flats = True
	else:
		config.flats = False

def set_scaletype(scaletype):
	config.scaletype = scaletype

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

