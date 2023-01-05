class __Midi__:
	def __init__(self):
		pass
	
	@classmethod
	def get_midi_nums(self, ranged_notes):
		lowest_midi_num = 21
		midi_nums = {}
		
		# build a dict of notes/midi nums
		counter = 0
		for note in ranged_notes:
			midi_nums[note] = lowest_midi_num + counter
			counter += 1
		
		return midi_nums