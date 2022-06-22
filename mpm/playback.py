#python3
# playback - a module for playing and transcribing midi using SCAMP

from scamp import Session
from mpm import config
#from melodic_pattern_maker import grid_guide


def play(): 
	# Creating session and parts
	s = Session()
	s.fast_forward_to_beat(500) # This makes it NOT play any sound
	s.tempo = config.tempo
	piano = s.new_part("piano")
	piano.clef_preference = config.clef.lower()

	# Transcribing
	s.start_transcribing()		

	# Rhythm numbers
	rhythm_to_num = {"quarter": 1, 
					"eighth": float(1/2), 
					"sixteenth": float(1/4), 
					"thirty second": float(1/8), 
					"triplet": float(1/3), 
					"sixteenth triplet": float(1/6)
					}
	a_rhythm_num = rhythm_to_num[config.a_rhythm]
	if config.b_rhythm != "":
		b_rhythm_num = rhythm_to_num[config.b_rhythm]
	
	# Choosing from flats or sharps list in config	
	if config.flats == True:
		selection = "flats"
	else:
		selection = "sharps"

	'''	# Setting final note
	first_note = config.exercise_list[0][0][0]
	last_note_range = int(config.exercise_list[-1][0][0][-1])
	final_note = first_note[:-1] + str(last_note_range + 1)
	final_note_midi_num = midi_nums[selection][final_note]'''


	# Playback and transcription
	for measure in config.exercise_list:
		measure_index = config.exercise_list.index(measure)
		
		for chunk in measure:
			chunk_index = measure.index(chunk)
			
			for note in chunk: 
				note_num = midi_nums[selection][note]

				if config.grid == True:
					if grid_guide[measure_index][chunk_index] == "a":
						dur = a_rhythm_num
					else:
						dur = b_rhythm_num
					piano.play_note(note_num, 1, dur)

				else:
					piano.play_note(note_num, 1, a_rhythm_num, f"key: {config.key_signature}")
	#piano.play_note(final_note_midi_num,1,1)
	performance = s.stop_transcribing()

	# Final print out 
	# <.show() will print in lilypond, .show_xml() will print in MuseScore
	performance.to_score(title = config.title, 
						composer = None, 
						time_signature=f"{config.beats}/{config.beattype}").show_xml()




