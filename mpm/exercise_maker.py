from mpm import config
from copy import copy
from mpm.logging_ import logger

#TODO Grid 
#TODO 'both' directions
#TODO Multiple Scales

def note_group_maker(startnote, measure_scale):
	"""Create a note group using a pattern key
	
	Keyword arguments: None
	Arguments: startnote, measure_scale
	Return: note_group
	"""
	note_group_scale = copy(measure_scale) # to be safe???
	start_note_index = note_group_scale.index(startnote)

	note_group = []
	
	for i in range(len(config.pattern)):
		# patterns are entered in human form (indexed from 1)
		# so we first change them to zero indexed
		pattern_note = (config.pattern[i]-1)
		note_index = start_note_index + pattern_note
		scale_note = note_group_scale[note_index]
		note_group.append(scale_note)
	
	return note_group

def measure_maker(startnote):
	"""Combine note groups to form a measure
	
	Keyword arguments: None
	Argument: startnote - assigned in run() method
	Return: measure
	"""
	measure = []
	
	measure_scale = config.ranged_scale
	
	if config.directions["measure"] == "down":
		measure_scale = measure_scale[::-1]
	
	start_note_index = measure_scale.index(startnote)

	for beat in range(config.beats):
		while True:
			note_group_startnote = measure_scale[start_note_index]
			note_group = note_group_maker(note_group_startnote, measure_scale)
			""" Removing "edge repeats"
				"Edge repeats" means the same note of two note_groups touching each other
				for example: [A,B,C][C,D,E] 
				we don't want that... so we skip over them except for the first notegroup
			"""
			if beat == 0:
				measure.append(note_group)
				start_note_index += 1
				break
			# all the rest
			if beat > 0:
				note_group_firstnote = note_group[0]
				previous_note_group_last_note = measure[beat-1][-1]

				if note_group_firstnote == previous_note_group_last_note:
					start_note_index += 1
					continue
				else:
					measure.append(note_group)
					start_note_index += 1
					break
	return measure


def get_exercise_list():
	"""Combine measures to create an exercise list
	
	Keyword arguments: None
	Return: exercise_list
	"""
	exercise_ranged_scale = config.ranged_scale
	if config.directions['exercise'] == "down":
		exercise_ranged_scale = exercise_ranged_scale[::-1]
	
	exercise_list = []
	
	start_note_index = exercise_ranged_scale.index(config.startnote) #first note of entire exercise

	for n in range(len(config.scale)):
		measure_startnote = exercise_ranged_scale[start_note_index]
		measure = measure_maker(measure_startnote)
		exercise_list.append(measure)
		start_note_index += 1
	
	return exercise_list