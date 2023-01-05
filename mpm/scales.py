from mpm.midi import __Midi__
from mpm.notes import __Notes__


class __Scale__:
	"""Return a Scale class object,
	should not be called by users
	User point of entry is <Chromatic> class
	
	Scale mostly acts as a building tool AFTER Chromatic class
	has been instantiated
	
	Keyword arguments: None
	"""
	
	def __init__(self, key):
		self.key = key.capitalize()
		self.flats_or_sharps = self.get_flats_or_sharps(key)
		
		# raw notes are an unsorted list of either sharps or flat
		self.raw_notes = __Notes__.get_raw_notes(self.flats_or_sharps)
		self.all_ranged_notes = __Notes__.get_ranged_notes(self.flats_or_sharps)
		
		# empty vars
		self.scale = []
		self.intervals = []
		self.midi_nums = {}

	def get_flats_or_sharps(self, key):
		flats = ["C","F","Bb","Eb","Ab","Db","Gb"]
		if key in flats:
			return "flats"
		else:
			return "sharps"
	
	def build_scale(self, range=8):
		# intervals are inherited from child class
		# scale is the inherited Chromatic.scale which we then 
		# choose intervals from
		self.scale = [self.scale[interval] for interval in self.intervals]
		self.rangify()
		self.assign_midi_nums()
	
	def rangify(self):
		self.ranged_scale = []
		self.ranged_scale = [ranged_note for ranged_note in self.all_ranged_notes 
							if ranged_note[:-1] in self.scale]

	def assign_midi_nums(self):
		all_midi_nums = __Midi__.get_midi_nums(self.all_ranged_notes)
		# selecting scale notes from all_midi_nums dict
		for n in self.ranged_scale:
			self.midi_nums[n] = all_midi_nums[n]



# Every class inherits from Chromatic
class Chromatic(__Scale__):
	"""Chromatic scale object, parent class of all scales
	Child of __Scale__ class.

	The real function of subclassing all other scales
	from the Chromatic scale (besides the fact that this
	is how scales are created in music theory) is that 
	Chromatic class sets the ORDER of the raw_scale.

	In this sense, the raw_scale isn't really a scale at all,
	it is just the notes in alphabetical order
	
	There may be a more programmatically correct way to build scales
	or store them, but this way actually follows the logic of music theory,
	so it's slightly easier to understand.
	
	It's possible to just store all of the scales in a database too
	Something to consider for the future...

	"""
	
	def __init__(self,key):
		# Chromatic class sets the order of its inherited raw_scale 
		# All children inherit their <scale> from the Chromtic <scale>
		super().__init__(key)
		self.scale = []
		
		key_index = self.raw_notes.index(self.key)
		
		# build chromatic scale
		# the modulo (%) trick handles any IndexErrors
		for i in range(len(self.raw_notes)):
			self.scale.append(self.raw_notes[(key_index + i) % len(self.raw_notes)])
		
		# note we don't call the buildscale() method ONLY for the Chromatic class
		# because we just did it up above
		self.rangify()
		self.assign_midi_nums()


# Basic Scales #
class Major(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0, 2, 4, 5, 7, 9, 11]
		self.build_scale()
		
class Minor(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0, 2, 3, 5, 7, 9, 10]
		self.build_scale()	

class MelodicMinor(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,2,3,5,7,8,11]
		self.build_scale()

# Penatonic Scales
class MajorPentatonic(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,2,4,7,9]
		self.build_scale()

class MinorPentatonic(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,3,5,7,10]
		self.build_scale()