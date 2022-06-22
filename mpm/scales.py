class __Scale__():
	"""Return a Scale class object,
	should not be called by users
	User point of entry is <Chromatic> class
	
	Keyword arguments: None
	Return: return_description
	"""
	
	def __init__(self, key):
		self.key = key.upper()
		self.allnotes = ["A","Bb","B","C","Db",
						"D","Eb","E","F","Gb",
						"G","Ab","A#","B","C",
						"C#","D","D#","E","F",
						"F#","G","G#"]

		# raw chromatic note sets
		flatsRawScale = ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab"]
		sharpsRawScale = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
		
		# Flats key or Sharp Key?
		if self.key in ["C","F","Bb","Eb","Ab","Db","Gb"]:
			self.flats_or_sharps = "flats"
			self.rawscale = flatsRawScale
		else:
			self.flats_or_sharps = "sharps"
			self.rawscale = sharpsRawScale

		
	
	# Rangify adds a range note onto each note of the scale
	# ex: C4, D4, E4, F4 etc...
	def rangify(self, scale_range):
		self.ranged_scale = [] #clearing
		for r in range(scale_range):
			for i in range(len(self.scale)):
				self.ranged_scale.append(self.scale[i] + str(r))

	def assign_midi_nums(self):
		lowest_midi_nums = {
						"sharps":{ 
							'A': 21, 'A#': 22, 'B': 23, 'C': 24, 'C#': 25, 'D': 26, 
							'D#': 27, 'E': 28, 'F': 29, 'F#': 30, 'G': 31, 'G#': 32
							},
						"flats":{ 
							'A': 21, 'Bb': 22, 'B': 23, 'C': 24, 'Db': 25, 'D': 26, 
							'Eb': 27, 'E': 28, 'F': 29, 'Gb': 30, 'G': 31, 'Ab': 32
							}
						}
		
		# easier to read for humans
		# ex: {"A1":21, "A#1":22, etc...
		self.midi_nums_dict = {}
		for n in range(len(self.ranged_scale)):
			note = self.ranged_scale[n]
			theNote = note[:-1]
			theRange = note[-1]
			lowest_midi_nums_for_note = lowest_midi_nums[self.flats_or_sharps][theNote]
			self.midi_nums_dict[note] = lowest_midi_nums_for_note + (int(theRange) * 12)
		
		self.midi_nums = list(self.midi_nums_dict.values())

	def buildScale(self, range=8):
		self.scale = [self.scale[interval] for interval in self.intervals]
		self.rangify(range)
		self.assign_midi_nums()


# Every class inherits from Chromatic
class Chromatic(__Scale__):
	"""Create a Chromatic scale object
	
	Keyword arguments:
	argument -- description
	Return: return_description
	"""
	
	def __init__(self,key):
		super().__init__(key)
		keyIndex = self.rawscale.index(self.key)
		offset = 0
		self.scale = []
		
		# Chromatic class sets the order of its inherited rawscale 
		# All children inherit <scale> from the Chromtic <scale>
		for i in range(len(self.rawscale)):
			try:
				self.scale.append(self.rawscale[keyIndex + i])
			except IndexError:
				self.scale.append(self.rawscale[0 + offset])
				offset += 1  
			
		self.rangify(9)
		self.assign_midi_nums()	
		self.chromaticScale = [note for note in self.scale]


# Basic Scales #
class Major(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0, 2, 4, 5, 7, 9, 11]
		self.buildScale()
		
class Minor(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0, 2, 3, 5, 7, 9, 10]
		self.buildScale()	

class MelodicMinor(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,2,3,5,7,8,11]
		self.buildScale()

# Penatonic Scales
class MajorPentatonic(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,2,4,7,9]
		self.buildScale()

class MinorPentatonic(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,3,5,7,10]
		self.buildScale()