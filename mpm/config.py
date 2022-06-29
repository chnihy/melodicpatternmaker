# config.py

class Config():
	def __init__(self):
		self.scale_object = None
		self.ranged_scale = None
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

class __Midi__():
	def __init__(self):
		self.midi_nums = {'flats': 
		{'A-1': 21, 'Bb-1': 22, 'B-1': 23, 
		'C0': 24, 'Db0': 25, 'D0': 26, 'Eb0': 27, 'E0': 28, 'F0': 29, 'Gb0': 30, 'G0': 31, 'Ab0': 32, 'A0': 33, 'Bb0': 34, 'B0': 35, 
		'C1': 36, 'Db1': 37, 'D1': 38, 'Eb1': 39, 'E1': 40, 'F1': 41, 'Gb1': 42, 'G1': 43, 'Ab1': 44, 'A1': 45, 'Bb1': 46, 'B1': 47, 
		'C2': 48, 'Db2': 49, 'D2': 50, 'Eb2': 51, 'E2': 52, 'F2': 53, 'Gb2': 54, 'G2': 55, 'Ab2': 56, 'A2': 57, 'Bb2': 58, 'B2': 59, 
		'C3': 60, 'Db3': 61, 'D3': 62, 'Eb3': 63, 'E3': 64, 'F3': 65, 'Gb3': 66, 'G3': 67, 'Ab3': 68, 'A3': 69, 'Bb3': 70, 'B3': 71, 'C4': 72, 'Db4': 73, 'D4': 74, 'Eb4': 75, 'E4': 76, 'F4': 77, 'Gb4': 78, 'G4': 79, 'Ab4': 80, 'A4': 81, 'Bb4': 82, 'B4': 83, 'C5': 84, 'Db5': 85, 'D5': 86, 'Eb5': 87, 'E5': 88, 'F5': 89, 'Gb5': 90, 'G5': 91, 'Ab5': 92, 'A5': 93, 'Bb5': 94, 'B5': 95, 'C6': 96, 'Db6': 97, 'D6': 98, 'Eb6': 99, 'E6': 100, 'F6': 101, 'Gb6': 102, 'G6': 103, 'Ab6': 104, 'A6': 105, 'Bb6': 106, 'B6': 107, 'C7': 108, 'Db7': 109, 'D7': 110, 'Eb7': 111, 'E7': 112, 'F7': 113, 'Gb7': 114, 'G7': 115, 'Ab7': 116, 'A7': 117, 'Bb7': 118, 'B7': 119, 'C8': 120, 'Db8': 121, 'D8': 122, 'Eb8': 123, 'E8': 124, 'F8': 125, 'Gb8': 126, 'G8': 127, 'Ab8': 128, 'A8': 129, 'Bb8': 130, 'B8': 131}, 'sharps': {'A-1': 21, 'A#-1': 22, 'B-1': 23, 'C0': 24, 'C#0': 25, 'D0': 26, 'D#0': 27, 'E0': 28, 'F0': 29, 'F#0': 30, 'G0': 31, 'G#0': 32, 'A0': 33, 'A#0': 34, 'B0': 35, 'C1': 36, 'C#1': 37, 'D1': 38, 'D#1': 39, 'E1': 40, 'F1': 41, 'F#1': 42, 'G1': 43, 'G#1': 44, 'A1': 45, 'A#1': 46, 'B1': 47, 'C2': 48, 'C#2': 49, 'D2': 50, 'D#2': 51, 'E2': 52, 'F2': 53, 'F#2': 54, 'G2': 55, 'G#2': 56, 'A2': 57, 'A#2': 58, 'B2': 59, 'C3': 60, 'C#3': 61, 'D3': 62, 'D#3': 63, 'E3': 64, 'F3': 65, 'F#3': 66, 'G3': 67, 'G#3': 68, 'A3': 69, 'A#3': 70, 'B3': 71, 'C4': 72, 'C#4': 73, 'D4': 74, 'D#4': 75, 'E4': 76, 'F4': 77, 'F#4': 78, 'G4': 79, 'G#4': 80, 'A4': 81, 'A#4': 82, 'B4': 83, 'C5': 84, 'C#5': 85, 'D5': 86, 'D#5': 87, 'E5': 88, 'F5': 89, 'F#5': 90, 'G5': 91, 'G#5': 92, 'A5': 93, 'A#5': 94, 'B5': 95, 'C6': 96, 'C#6': 97, 'D6': 98, 'D#6': 99, 'E6': 100, 'F6': 101, 'F#6': 102, 'G6': 103, 'G#6': 104, 'A6': 105, 'A#6': 106, 'B6': 107, 'C7': 108, 'C#7': 109, 'D7': 110, 'D#7': 111, 'E7': 112, 'F7': 113, 'F#7': 114, 'G7': 115, 'G#7': 116, 'A7': 117, 'A#7': 118, 'B7': 119, 'C8': 120, 'C#8': 121, 'D8': 122, 'D#8': 123, 'E8': 124, 'F8': 125, 'F#8': 126, 'G8': 127, 'G#8': 128, 'A8': 129, 'A#8': 130, 'B8': 131}}

class Grid():
	def __init__(self):
		self.grid_guide = [
			["a", "b", "b", "b"], 	
			["b", "a", "b", "b"], 
			["b", "b", "a", "b"], 
			["b", "b", "b", "a"]]

