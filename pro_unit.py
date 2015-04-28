
class ProUnit():
	"""
	process one pipeline step
	"""

	def __init__(self):
		self._regA = []
		self._regB = []
		self._regP = []
		self._empty = True
		self._counter = 0

	def start(self, divident, divider):
		self._regA = divident
		self._regB = divider
		self._regP = [0 for digit in self._regA]
		self._regP.append(0)
		self._counter = 0
		self._empty = False

	def shift(self):
		"""
		perform shift of pair <regP, regA>
		"""
		self._regP.pop()
		self._regP.insert(0, self._regA.pop())

	def subtract(self, minuend, subtrahend):
		"""
		perform subtraction
		"""

		copy_subtrahend = list(subtrahend)
		if len(copy_subtrahend) < len(minuend):
			while len(copy_subtrahend) != len(minuend):
				copy_subtrahend.append(0)

		ones_comp = [(lambda number: 1 if number == 0 else 0)(number)
		 	for number in copy_subtrahend]

		twos_comp = self.add(minuend, ones_comp) 
		return self.add(twos_comp, [1])

	def single_digit_add(self, first, second, transfer):
		"""
		accept first and second as binary values and transfer as boolean value
		perform single digit addition, return tuple (result, transfer)
		"""

		value = first + second
		if transfer:
			value += 1

		if value > 2:
				result = 1
				transfer = True
		elif value < 2:
			result = value
			transfer = False
		else:
			result = 0
			transfer = True

		return (result, transfer)


	def add(self, first, second):
		"""
		perform addition
		"""

		copy_first = list(first)
		copy_second = list(second)

		result = []
		transfer = False

		while len(copy_first) > 0 and len(copy_second) > 0:
			temp = self.single_digit_add(copy_first.pop(0), copy_second.pop(0),
				transfer)
			result.append(temp[0])
			transfer = temp[1]
			
		if len(copy_first) > 0:
			while len(copy_first) > 0:
				temp = self.single_digit_add(copy_first.pop(0), 0, transfer)
				result.append(temp[0])
				transfer = temp[1]
		if len(copy_second) > 0:
			while len(copy_second) > 0:
				temp = self.single_digit_add(0, copy_second.pop(0), transfer)
				result.append(temp[0])
				transfer = temp[1]

		return result

	def is_regP_positive(self):
		"""
		check if regP is positive
		"""
		return True if self._regP[len(self._regP) - 1] == 0 else False

	def perform_step(self):
		"""
		perform one step of non-restoring division
		"""

		if self.is_regP_positive():
			self.shift()
			self._regP = self.subtract(self._regP, self._regB)
		else:
			self.shift()
			self._regP = self.add(self._regP, self._regB)

		if self.is_regP_positive():
			self._regA.insert(0, 1)
		else:
			self._regA.insert(0, 0)

		self._counter += 1

		if self._counter == len(self._regA):
			if not self.is_regP_positive():
				self._regP = self.add(self._regP, self._regB)
			self._counter = 0
			self._empty = True

	def get_regP(self):
		return self._regP

	def get_regA(self):
		return self._regA

	def get_regB(self):
		return self._regB

	def is_empty(self):
		return self._empty

class Clock():
	
	def __init__(self, start_time):
		self._time = start.time

	def tick(self):
		"""
		perform one tick
		"""
		self._time += 1

	def get_current_time(self):
		return self._time
