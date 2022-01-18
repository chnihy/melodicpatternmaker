#! python
from pprint import pprint
from copy import copy
import scales
import config

#--------- TODO ----------#

#---------  GLOBAL VARIABLES  -------------#
grid_guide = [["a","b","b","b"],	
			["b","a","b","b"],
			["b","b","a","b"],
			["b","b","b","a"]]

pattern_scale_relation_combo_flag = False

psr_counter = False

# Pattern scale combos counter
def counter_run(counter):
	if counter == False:
		counter = True
		return counter
	
	if counter == True:
		counter = False
		return counter

# Rangify adds a range number after each note of the scale. So "C" becomes "C3", "D"  becomes "D3", etc...
def rangify(scale, flats):
	ranged_scale = []
	
	# Flats or sharps from scales.py
	if flats == True:
		selection = "flats"
	else:
		selection = "sharps"
	
	# Adding numbers 1-9 to selected scale
	for i in range(9):
		for note in scales.allnotes_ranged[selection]:
			if note[:-1] in scale:
				ranged_scale.append(note)
	
	return ranged_scale


# Multi Scale Combiner combines two scales into one list, in alternating measures.  
def multi_scale_combiner(exlist1, exlist2):
	combined_exercise_list = []
	
	for i in range(len(exlist1)):
		if i % 2 == 0:
			combined_exercise_list.append(exlist1[i])
		else:
			combined_exercise_list.append(exlist2[i])
	
	return combined_exercise_list


#---------  MINI MODULES  -------------#
def chunk_pattern_key_maker(pattern):
	pattern_to_chunk_dict = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven"}
	
	chunk_pattern_key = []
	
	# Converting 
	for num in pattern:
		chunk_pattern_key.append(pattern_to_chunk_dict[num])
	
	return chunk_pattern_key


def chunk_maker(startnote, measure_scale, chunk_pattern_key):
	# Variables
	# Note offsets are added to Start Note Index in our chunk
	note_offsets = ["one","two","three","four","five","six","seven"] 
	
	chunk_scale = copy(measure_scale) #just to be safe
	
	# Starting note index
	sni = chunk_scale.index(startnote)
	
	chunk = []
	
	# fill chunk with placeholders
	for i in range(len(chunk_pattern_key)):
		chunk.append("") 

	# Creating chunk
	for i, var in enumerate(chunk_pattern_key):
		for offset, note in enumerate(note_offsets):
			if var == note:
				try:
					chunk[i] = chunk_scale[sni + offset]
				except IndexError:
					print("Chunk maker out of range! ")
	
	return chunk

def measure_maker(ranged_scale, 
					measure_direction, 
					pattern_scale_relation,
					startnote, 
					chunk_pattern_key_a, 
					chunk_pattern_key_b, 
					measure_grid_guide, 
					beats, 
					grid):	

	# TODO why is this here? Duplicate?
	def counter_run(counter):
		if counter == False:
			counter = True
			return counter
		
		if counter == True:
			counter = False
			return counter
	
	# Pattern Scale Relations
	global pattern_scale_relation_combo_flag
	
	if pattern_scale_relation == "complimentary_contrary":
		pattern_scale_relation_combo_flag = True
		contrary_chunk_counter = False
	
	if pattern_scale_relation == "contrary_complimentary":
		pattern_scale_relation_combo_flag = True
		contrary_chunk_counter = True

	# Chunk Flipper
	def contrary(chunk):
		chunk = [note for note in chunk[::-1]]
		return chunk

	# Variables
	measure = []
	
	# Scale Construction
	measure_scale = copy(ranged_scale) #making a copy prevents chunk, measure and exercisemaker from re-flipping the same scale...
	
	if measure_direction == "down":
		measure_scale = measure_scale[::-1]
	
	# Starting Note Index 
	sni = measure_scale.index(startnote)

	# Ye holy algorithm
	for beat in range(beats):
		
		while True:
			# Checking grid guide
			if grid == True:
				if measure_grid_guide[beat] == "a":
					chunk_pattern_key = chunk_pattern_key_a
				
				if measure_grid_guide[beat] == "b":
					chunk_pattern_key = chunk_pattern_key_b	
			else:
				chunk_pattern_key = chunk_pattern_key_a
		
			# Building Chunk
			try:
				startnote = measure_scale[sni]
				chunk = chunk_maker(startnote, measure_scale, chunk_pattern_key)
			
			except IndexError:
				print("Out of Range! ")
				break
		
			# If contrary/complimentary motion
			if pattern_scale_relation_combo_flag == True: 
				if contrary_chunk_counter == True:
					chunk = contrary(chunk)
				contrary_chunk_counter = counter_run(contrary_chunk_counter)
			
			# If just contrary motion
			if pattern_scale_relation == "contrary":
				chunk = contrary(chunk)
			
			if pattern_scale_relation == "complimentary":
				pass
		
			# Removing chunk edge repeats
			# Edge repeats mean the same note on two chunks touching each other
			# for example [A,B,C][C,D,E] - we don't want that... so we remove them
			# We skip this for the first chunk
			if beat == 0: 
				measure.append(chunk)
				sni += 1 
				break	
			# All the rest...
			else: 
				chunk_first_note = chunk[0]
				chunk_last_note = chunk[-1]
				previous_chunk_first_note = measure[beat-1][0]
				previous_chunk_last_note = measure[beat-1][-1]
				
				# If edge repeat detected, go to the next note of the scale and start over
				if chunk_first_note == previous_chunk_last_note: 
					sni += 1 
					continue
				else:
					measure.append(chunk)
					sni += 1
					break	

	return measure

def exercise_maker( beats,
					root,
					scaletype,
					flats,
					startnote, 
					pattern,
					a_rhythm ,
					measure_direction, 
					exercise_direction, 
					grid, 
					b_rhythm,
					b_pattern, 
					grid_scale_motion,
					pattern_scale_relation, 
					multi_scale
					):
	
	# Variables
	scale = scales.allscales[scaletype][root]

	ranged_scale = rangify(scale, flats)
	
	exercise_list = []

	# Making a copy of scale for exercise maker
	if exercise_direction == "down":
		exscale = copy(ranged_scale[::-1])
	else:
		exscale = copy(ranged_scale)

	# Starting Note Index
	sni = exscale.index(startnote)

	# Making our chunk pattern key(s)
	chunk_pattern_key_a = chunk_pattern_key_maker(pattern)
	
	if grid == True:
		chunk_pattern_key_b = chunk_pattern_key_maker(b_pattern)
	else:
		chunk_pattern_key_b = None
	
	
	#---- Ye holy algorithm ----#
	# Grid exercise list
	if grid == True:
		for meas in range(len(grid_guide)):
			measure_grid_guide = grid_guide[meas]
			
			# One way measure direction
			if measure_direction == "up" or measure_direction == "down" :
				try:
					startnote = exscale[sni]
				
				except IndexError:
					print("Out of Range! ")
				
				# This is "up" for either way, because our scale will be flipped for 'down' in our function already
				one_way_measure = measure_maker(ranged_scale, "up", pattern_scale_relation, startnote, chunk_pattern_key_a, chunk_pattern_key_b, measure_grid_guide, beats, grid)

				# Add measure to exlist
				exercise_list.append(one_way_measure)
				
				# Grid scale motion determines if startnote increments or stays
				if grid_scale_motion == "follow":
					sni += 1
				if grid_scale_motion == "stay":
					pass
			
			# If Measure direction is both
			if measure_direction == "both":
				
				# Going up
				try:
					startnote = exscale[sni]
				except IndexError:
					print("Out of Range!")				
				
				going_up = measure_maker(ranged_scale, "up", pattern_scale_relation, startnote, chunk_pattern_key_a, chunk_pattern_key_b, measure_grid_guide, beats, grid)
				
				# Going down
				try:
					lastnote_going_up_index = exscale.index(going_up[-1][-1])
					# Going down from the note above the last note of prev measure - eliminates doubled notes
					descending_note = exscale[lastnote_going_up_index + 1] 
				except IndexError:
					print("Out of range! ")
				
				going_down = measure_maker(ranged_scale, "down", pattern_scale_relation, descending_note, chunk_pattern_key_a, chunk_pattern_key_b, measure_grid_guide, beats, grid)

				exercise_list.append(going_up)
	
				exercise_list.append(going_down)

				# Grid scale motion determines start note
				if grid_scale_motion == "follow":
					sni = exscale.index(going_down[-1][-1])+1 # Eliminates doubled notes
				if grid_scale_motion == "stay":
					pass

	# Exercise Maker without Grid
	if grid == False:
		measure_grid_guide = None
		
		for note in scale:	
			
			# One way measure direction
			if measure_direction == "up" or measure_direction == "down":			
				try:
					startnote = exscale[sni]
				except IndexError:
					print("Out of Range! ")
				
				one_way_measure = measure_maker(ranged_scale, 
												measure_direction, 
												pattern_scale_relation, 
												startnote, 
												chunk_pattern_key_a,
												chunk_pattern_key_b, 
												measure_grid_guide, 
												beats, 
												grid)

				# Add measure to exlist
				exercise_list.append(one_way_measure)
				sni += 1
			
			# If scale direction is 'both'
			if measure_direction == "both":
			
				# Going up
				try:
					startnote = exscale[sni]
				except IndexError:
					print("Out of range! ")
				going_up = measure_maker(ranged_scale, 
										"up", 
										pattern_scale_relation, 
										startnote, 
										chunk_pattern_key_a, 
										chunk_pattern_key_b, 
										measure_grid_guide, 
										beats, 
										grid)
				
				# Going down
				try:
					lastnote_going_up_index = exscale.index(going_up[-1][-1])
					descending_note = exscale[lastnote_going_up_index + 1] #GOING DOWN FROM THE NOTE ABOVE THE LAST NOTE OF PREV MEASURE - eliminates doubled notes
				except IndexError:
					print("Out of Range! ")
				going_down = measure_maker(ranged_scale, "down", pattern_scale_relation, descending_note, chunk_pattern_key_a, chunk_pattern_key_b, measure_grid_guide, beats, grid)
				
				# GOING UP STARTS FROM 1 STEP ABOVE LAST NOTE OF GOING DOWN - eliminates doubled notes
				lastnote_going_down = copy(going_down[-1][-1])
				sni = exscale.index(lastnote_going_down) + 1 

				# Add to ex list
				exercise_list.append(going_up)
				exercise_list.append(going_down)
	
	# Updating config
	config.a_rhythm = a_rhythm
	config.b_rhythm = b_rhythm
	config.grid = grid
	
	if multi_scale == True:
		config.exercise_list_2 = exercise_list
		config.combined_exercise_list = multi_scale_combiner(config.exercise_list, config.exercise_list_2)
	else:
		config.exercise_list = exercise_list

#---------  FINAL TESTING  -------------#
#chunk_pattern_key_a = ["one","two","three","four"], chunk_pattern_key_b = ["one","three"], startnote = "c4"
"""testing = {"exercise_direction":["up","down"],
			"scale_direction":["up","down","both"],
			"pattern_scale_relation":["complimentary","contrary","complimentary_contrary","contrary_complimentary"],
			"grid": [False],
			"grid_scale_motion":["stay","follow"]
			} #TODO ADD GRID VAR

xn = 1
for g in testing["grid"]:
	for esd in testing["exercise_direction"]:
		for sd in testing["scale_direction"]:
			for psr in testing["pattern_scale_relation"]:
				print(str(xn))
				print(f"EXERCISE DIRECTION: {esd}")
				print(f"SCALE DIRECTION: {sd}")
				print(f"PATTERN_SCALE_RELATION: {psr}")
				#print(f"GRID: {g}, MOTION: follow")
				print(f"GRID: {g}, MOTION: stay")
				exercise_maker(chunk_pattern_key_a=['one','two','three','four'],  scale_direction=sd, startnote = "c3", exercise_direction=esd, pattern_scale_relation=psr, grid=g, grid_scale_motion="stay")
				xn += 1
				pattern_scale_relation_combo_flag = False
				print("")
				print("")"""

