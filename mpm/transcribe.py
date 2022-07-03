# playback.py

from scamp import Session
from mpm import config
from mpm.config import Rhythm
from mpm.logging_ import logger
#from melodic_pattern_maker import grid_guide


def run(): 
	s = Session()
	s.fast_forward_to_beat(500) # This makes it NOT play any sound
	s.tempo = config.tempo
	piano = s.new_part("piano")
	piano.clef_preference = config.clef.lower()
	rhythm_nums = Rhythm().rhythm_nums	

	s.start_transcribing()		

	a_rhythm_num = rhythm_nums[config.a_rhythm]
	if config.b_rhythm != None:
		b_rhythm_num = rhythm_nums[config.b_rhythm]

	'''	# Setting final note
	first_note = config.exercise_list[0][0][0]
	last_note_range = int(config.exercise_list[-1][0][0][-1])
	final_note = first_note[:-1] + str(last_note_range + 1)
	final_note_midi_num = midi_nums[selection][final_note]'''


	# Playback and transcription
	for midi_num in config.exercise_list_midi_nums:
		piano.play_note(midi_num, 1, a_rhythm_num, f"key: {config.key_signature}")
		
		'''if config.grid == True:
			if grid_guide[measure_index][chunk_index] == "a":
				dur = a_rhythm_num
			else:
				dur = b_rhythm_num
			piano.play_note(note_num, 1, dur)

		else:
			piano.play_note(note_num, 1, a_rhythm_num, f"key: {config.key_signature}")'''
	#piano.play_note(final_note_midi_num,1,1)
	performance = s.stop_transcribing()

	# Final print out 
	# show() will print in lilypond, show_xml() will print in MuseScore
	performance.to_score(title = config.title, 
						composer = None, 
						time_signature=f"{config.beats}/{config.beat_type}").show_xml()




