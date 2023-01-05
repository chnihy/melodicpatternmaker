class __Notes__:
	"""Notes class, used by scales to get ranged scales

	"""
	def __init__(self):
		pass
	
	@classmethod
	def get_raw_notes(self, flats_or_sharps):
		raw_notes = {"all": ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab","A#","C#","D#","F#","G#"],
						"flats": ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab"],
						"sharps": ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]}
		return raw_notes[flats_or_sharps]
			
	@classmethod
	def get_ranged_notes(self, flats_or_sharps):
		range_nums = ["-1","0","1","2","3","4","5","6","7","8"]
		ranged_notes = []
		
		# build 
		for range_num in range_nums:
			for note in self.get_raw_notes(flats_or_sharps):
				ranged_notes.append(note + range_num)
		
		# we return the list without the notes that don't exist in the musical score
		return ranged_notes[12:-4]