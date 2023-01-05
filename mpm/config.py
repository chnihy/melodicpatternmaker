class Config:
	def __init__(self):
		self.scale_object = None
		self.ranged_scale = None
		#self.ranged_scale_exercise = None
		self.ranged_scale_measure = None
		self.scale = None
		self._exercise_list = []
		self.exercise_list_midi_nums = None

		# Time
		self.tempo = None
		self.beats = None
		self.beat_type = None

		# Scale/Key
		self.range = None
		self.key_signature = None
		self.root = None
		self.flats = True
		self.flats_or_sharps = None
		self.scaletype = None
		self.startnote = None
		self.range_start = None
		self.clef = None
	
		# Pattern/Rhythm
		self.pattern = None
		self.a_rhythm = None
		
		# Directions
		self.directions = {"measure": None, "exercise": None}
		
		# Grid
		self.grid = False
		self.b_pattern = None
		self.b_rhythm = None
		self.grid_scale_motion = None
		
		self.title = None
		

	@property
	def exercise_list(self):
		return self._exercise_list
			
	@exercise_list.setter
	def exercise_list(self, new_list):
		self._exercise_list = new_list
