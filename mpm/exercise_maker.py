from mpm import config
from copy import copy

#TODO Grid 
#TODO 'both' directions

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
		# patterns are entered in human form (starting with 1)
		# so we first change them to array indexed (starting a 0)
		pattern_note = (config.pattern[i]-1)
		note_index = start_note_index + pattern_note
		scale_note = note_group_scale[note_index]
		note_group.append(scale_note)
	return note_group

def measure_maker(startnote):
	"""Combine note groups to form a measure
	
	Keyword arguments: None
	Argument: startnote
	Return: measure
	"""
	measure = []
	measure_scale = copy(config.ranged_scale) # to be safe???
	if config.directions["measure"] == "down":
		measure_scale = measure_scale[::-1]
	start_note_index = measure_scale.index(startnote)

	for beat in range(config.beats):
		while True:
			note_group_startnote = measure_scale[start_note_index]
			note_group = note_group_maker(note_group_startnote, measure_scale)
			# Removing "edge repeats"
			# "Edge repeats" means the same note of two noteGroups touching each other
			# for example: [A,B,C][C,D,E] we don't want that... so we skip over them
			# except for the first notegroup
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


def run():
	"""Combine measures to create an exercise list
	
	Keyword arguments: None
	Return: exercise_list
	"""
	exercise_list = [] #clearing
	start_note_index = config.ranged_scale.index(config.startnote) #first note of exercise
	
	for n in range(len(config.scale)):
		measure_startnote = config.ranged_scale[start_note_index]
		measure = measure_maker(measure_startnote)
		exercise_list.append(measure)
		start_note_index += 1
	
	return exercise_list