import pro_unit

class Pipeline():
	"""
	implements pipeline for division
	"""

	def __init__(self, rang, list_of_numbers):

		self._units = []
		for dummy_idx in range(rang):
			self._units.append(pro_unit.ProUnit())

		self._numbers = list(list_of_numbers)
		self._result = []
		self._clock = Clock(0)

	def perform_stage(self):
		"""
		start division
		"""

		for unit in self._units:
			if unit.is_empty():
				quatient = unit.get_regA()
				remainder = unit.get_regP()

				if len(quatient) > 0 and len(remainder) > 0:
					self._result.append((quatient, remainder))

				pair = self._numbers.pop(0)

				unit.start(pair[0], pair[1])
			else:
				unit.perform_step()

		self._clock.tick()

