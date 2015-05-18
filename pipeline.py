import pro_unit
import clock

class Pipeline():
	"""
	implements pipeline for division
	"""

	def __init__(self):

		self._rang = 0
		self._digits = 0
		self._units = []
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

	def start(self, rang, digits, list_of_numbers):
		"""
		starts pipeline with given parameters
		"""
		self._rang = rang
		self._digits = digits
		self._numbers = []
		self._units = []
		for dummy_idx in range(digits):
			self._units.append(pro_unit.ProUnit())
		self._units[len(self._units) - 1].last(True)
		self._units[0].set_duration(2)
		self._units[len(self._units) - 1].set_duration(3)
		for pair in list_of_numbers:
			first = self.int_to_bin_list(pair[0])
			second = self.int_to_bin_list(pair[1])
			self._numbers.append((first, second))
		self._result = []
		self._clock.reset()

	def perform_stage(self):
		"""
		performs one stage
		"""
		if not self.is_active():
			return

		last = self._units[len(self._units) - 1]

		if not last.is_empty():
			quatient = self.bin_list_to_int(last.get_regA())
			remainder = self.bin_list_to_int(last.get_regP())
			self._result.append((quatient, remainder))

		for idx in range(len(self._units) - 1, -1, -1):
			if idx == 0:
				self._units[idx].active(True)
				if len(self._numbers) != 0 and not self.is_full():
					pair = self._numbers.pop(0)
					remainder = [0 for digit in pair[0]]
					remainder.append(0)
					self._units[idx].load(pair[0], pair[1], remainder)
					self._units[idx].perform_step()
					if not self._units[idx].is_active():
						self._units[idx].active(True)
				else:
					self._units[idx].reset()
			elif self._units[idx - 1].is_active():
				self._units[idx].load(self._units[idx - 1].get_regA(),
					self._units[idx - 1].get_regB(),
					self._units[idx - 1].get_regP())
				self._units[idx].perform_step()
				if not self._units[idx].is_active():
					self._units[idx].active(True)
			else:
				self._units[idx].reset()

		if self.is_active():
			durations = [unit.get_duration() for unit in self._units
			if unit.is_active()]
			self._clock.tick(max(durations))

	def int_to_bin_list(self, num):
		"""
		converts integer to reversive binary list
		"""
		bin_number = bin(num)
		bin_number = bin_number[2:]

		bin_list = list(bin_number)
		bin_list = [int(value) for value in bin_list]
		bin_list.reverse()

		while len(bin_list) != self._digits:
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
				if not unit.is_empty():
					return True
			return False
		return True


	def is_full(self):

		counter = 0
		for unit in self._units:
			if unit.is_active():
				counter += 1

		if counter > self._rang:
			return True
		else:
			return False
			
	def get_result(self):
		return self._result

	def get_time(self):
		return self._clock.get_current_time()



