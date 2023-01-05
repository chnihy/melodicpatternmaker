class Grid():
	def __init__(self):
		self.grid_guide = [
			["a", "b", "b", "b"], 	
			["b", "a", "b", "b"], 
			["b", "b", "a", "b"], 
			["b", "b", "b", "a"]]
	
	@property
	def stacking_grid(self):
		grid_guide = [
			["a", "b", "b", "b"], 	
			["b", "a", "b", "b"], 
			["b", "b", "a", "b"], 
			["b", "b", "b", "a"]]
		return grid_guide
