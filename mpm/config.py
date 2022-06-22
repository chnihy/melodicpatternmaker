#config.py

class Config():
	def __init__(self):
		self.scale_object = None
		self.scale = None
		self.ranged_scale = None
		self.range = None
		self._exercise_list = []
		self.startnote = None
		self.range_start = "0"
		self.clef = "treble"
		
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
		
		self.title = None

	@property
	def exercise_list(self):
		for i in self._exercise_list:
			print(i)
			
	@exercise_list.setter
	def exercise_list(self, new_list):
		self._exercise_list = new_list

class Rhythm():
	rhythms = ["quarter", "eighth", "triplet", "sixteenth", "sixteenth triplet", "thirty second"]