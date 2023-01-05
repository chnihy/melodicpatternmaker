class Rhythm:
	"""Rhythm class contains general rhythmic translations and float values
	"""
	def __init__(self):
		pass
		
	@classmethod
	def get_rhythms(self):
		rhythms = ["quarter", "eighth", "triplet", "sixteenth", "sixteenth triplet", "thirty second"]
		return rhythms
		
	@classmethod
	def get_rhythm_nums(self):
		rhythm_nums = {"quarter": 1, 
						"eighth": float(1/2), 
						"sixteenth": float(1/4), 
						"thirty second": float(1/8), 
						"triplet": float(1/3), 
						"sixteenth triplet": float(1/6)}
		return rhythm_nums

