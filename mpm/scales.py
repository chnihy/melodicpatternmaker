from mpm.config import __Midi__
from mpm.notes import __Notes__


class __Scale__():
	"""Return a Scale class object,
	should not be called by users
	User point of entry is <Chromatic> class
	
	Keyword arguments: None
	Return: return_description
	"""
	
	def __init__(self, key):
		self.key = key.capitalize()
		# Flats key or Sharp Key?
		if self.key in __Notes__().flats_raw_notes:
			self.flats_or_sharps = "flats"
			self.raw_notes = __Notes__().flats_raw_notes
		else:
			self.flats_or_sharps = "sharps"
			self.raw_notes = __Notes__().sharps_raw_notes

	def rangify(self):
		self.ranged_scale = []
		for ranged_note in __Notes__().all_notes_ranged[self.flats_or_sharps]:
			if ranged_note[:-1] in self.scale:
				self.ranged_scale.append(ranged_note)

	def assign_midi_nums(self):		
		self.midi_nums = {}
		for n in self.ranged_scale:
			self.midi_nums[n] = __Midi__().midi_nums[self.flats_or_sharps][n]

	def build_scale(self, range=8):
		self.scale = [self.scale[interval] for interval in self.intervals]
		self.rangify()
		self.assign_midi_nums()
		


# Every class inherits from Chromatic
class Chromatic(__Scale__):
	"""Create a Chromatic scale object

	The real function of subclassing all other scales
	from the Chromatic scale (besides the fact that this
	is how scales are created in music theory) is that 
	Chromatic class sets the ORDER of the raw_scale.

	In this sense, the raw_scale isn't really a scale at all,
	it is just the notes in alphabetical order
	
	"""
	
	def __init__(self,key):
		# Chromatic class sets the order of its inherited raw_scale 
		# All children inherit their <scale> from the Chromtic <scale>
		super().__init__(key)
		key_index = self.raw_notes.index(self.key)
		offset = 0
		
		self.scale = []
		for i in range(len(self.raw_notes)):
			try:
				self.scale.append(self.raw_notes[key_index + i])
			except IndexError:
				self.scale.append(self.raw_notes[0 + offset])
				offset += 1  

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