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
		self._active = False

	def __str__(self):

		result = "Time: " + str(self._clock) + "\n"

		for unit in self._units:
			result += str(unit) + "\n"

		return result

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
		self._active = True

		for unit in self._units:
			unit.reset()

	def perform_stage(self):
		"""
		performs one stage
		"""

		print(len(self._numbers))
		units = self._units	
		if len(self._numbers) == 0:
			active_check = False
			for unit in units:
				if not unit.is_empty():
					active_check = True
					break
			if not active_check:
				self._active = False
				return

		loaded = False

		for unit_idx in range(len(units)):
			if unit_idx >= self._rang:
				break;
			if units[unit_idx].is_empty():
				quatient = units[unit_idx].get_regA()
				remainder = units[unit_idx].get_regP()

				if len(quatient) > 0 and len(remainder) > 0:
					first = self.bin_list_to_int(quatient)
					second = self.bin_list_to_int(remainder)
					self._result.append((first, second))
					units[unit_idx].reset()

				if len(self._numbers) > 0 and not loaded:
					pair = self._numbers.pop(0)
					units[unit_idx].start(pair[0], pair[1])
					loaded = True
			else:
				units[unit_idx].perform_step()
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
		return self._active

	def get_result(self):
		return self._result



