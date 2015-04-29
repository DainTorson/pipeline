class Clock():
	"""
	implements clock
	"""
	
	def __init__(self):
		self._time = 0

	def __str__(self):
		return str(self._time)

	def tick(self):
		"""
		perform one tick
		"""
		self._time += 1

	def get_current_time(self):
		return self._time

	def reset(self):
		"""
		resets time to 0
		"""
		self._time = 0

	def set_time(self, time):
		self._time = time
