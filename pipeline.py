import pro_unit
import clock

class Pipeline():
	"""
	implements pipeline for division
	"""

	def __init__(self):

		self._num_of_processors = 8
		self._rang = self._num_of_processors
		self._units = []
		for dummy_idx in range(self._num_of_processors):
			self._units.append(pro_unit.ProUnit())
		self._numbers = []
		self._result = []
		self._clock = clock.Clock()

	def __str__(self):

		result = "Time: " + str(self._clock) + "\n"

		for unit in self._units:
			result += str(unit) + "\n"

		return result

	def __iter__(self):

		for unit in self._units:
			yield unit

	def start(self, rang, list_of_numbers):
		"""
		starts pipeline with given parameters
		"""
		self._rang = rang
		self._numbers = []
		for pair in list_of_numbers:
			first = self.int_to_bin_list(pair[0])
			second = self.int_to_bin_list(pair[1])
			self._numbers.append((first, second))
		self._result = []
		self._clock.reset()
		
		for unit in self._units:
			unit.reset()

	def perform_stage(self):
		"""
		performs one stage
		"""

		if not self.is_active():
			print("not active")
			return

		loaded = False #checks if any pair has been loaded on that stage(only one load allowed)
		unit_idx = 0
		for unit in self._units:
			if unit_idx >= self._rang:
				break
			if unit.is_active():
				unit.perform_step()
			else:
				if unit.is_empty():
					if len(self._numbers) > 0 and not loaded:
						pair = self._numbers.pop(0)
						unit.load(pair[0], pair[1])
						loaded = True
				else:
					quatient = self.bin_list_to_int(unit.get_regA())
					remainder = self.bin_list_to_int(unit.get_regP())
					self._result.append((quatient, remainder))
					unit.reset()
			unit_idx += 1
		self._clock.tick()

	def int_to_bin_list(self, num):
		"""
		converts integer to reversive binary list
		"""
		bin_number = bin(num)
		bin_number = bin_number[2:]

		bin_list = list(bin_number)
		bin_list = [int(value) for value in bin_list]
		bin_list.reverse()

		while len(bin_list) != 8:
			bin_list.append(0)

		return bin_list

	def bin_list_to_int(self, blist):
		"""
		converts reversive binary list to integer
		"""

		bin_list = list(blist)
		bin_list.reverse()
		bin_list = ''.join(str(value) for value in bin_list)

		return int(bin_list, 2)

	def is_active(self):
		if len(self._numbers) == 0:
			for unit in self._units:
				if unit.is_active() or not unit.is_empty():
					return True
			return False
		return True

	def get_result(self):
		return self._result

	def get_time(self):
		return self._clock.get_current_time()



