#config.py

class Config():
	def __init__(self):
		self.scale_object = None
		self.ranged_scale = None
		self.scale = None
		self.range = 8
		self._exercise_list = []
		self.grid_guide = [
			["a","b","b","b"],	
			["b","a","b","b"],
			["b","b","a","b"],
			["b","b","b","a"]]

		# Time
		self.tempo = 120
		self.beats = 4
		self.beat_type = 4

		# Scale/Key
		self.key_signature = "C major"
		self.root = "C"
		self.flats = True
		self.scaletype = "Major"
		self.startnote = "C" #this will be just the Note 
		self.range_start = "4"
		self.clef = "treble"
	
		# Pattern/Rhythm
		self.pattern = [1,2,3,4]
		self.a_rhythm = "sixteenth"
		
		# Directions
		self.directions = {"measure": "up","exercise": "up"}
		
		# Grid
		self.grid = False
		self.b_pattern = None
		self.b_rhythm = None
		self.grid_scale_motion = None
		
		self.title = "Default Title"
		'''self.scale_object = None
		self.scale = None
		self.ranged_scale = None
		self.range = None
		self._exercise_list = []
		self.startnote = None
		self.range_start = "0"
		self.clef = "treble"
		self.grid_guide = [
			["a","b","b","b"],	
			["b","a","b","b"],
			["b","b","a","b"],
			["b","b","b","a"]]

		# Time
		self.tempo = None
		self.beats = None
		self.beat_type = None

		# Scale/Key
		self.key_signature = None
		self.root = None
		self.flats = True
		self.scaletype = None
		self.startnote = None
	
		# Pattern/Rhythm
		self.pattern = None
		self.a_rhythm = None
		
		# Directions
		self.directions = {"measure": None,"exercise": None}
		
		# Grid
		self.grid = False
		self.b_pattern = None
		self.b_rhythm = None
		self.grid_scale_motion = None
		
		self.title = None'''

	@property
	def exercise_list(self):
		for i in self._exercise_list:
			print(i)
		return self._exercise_list
			
	@exercise_list.setter
	def exercise_list(self, new_list):
		self._exercise_list = new_list


class Rhythm():
	rhythms = ["quarter", "eighth", "triplet", "sixteenth", "sixteenth triplet", "thirty second"]
	# Rhythm numbers
	rhythm_nums = {"quarter": 1, 
					"eighth": float(1/2), 
					"sixteenth": float(1/4), 
					"thirty second": float(1/8), 
					"triplet": float(1/3), 
					"sixteenth triplet": float(1/6)}