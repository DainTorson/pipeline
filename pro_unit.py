
class ProUnit():
	"""
	implements processing unit, which process one pipeline step
	"""

	def __init__(self):

		self._regA = []
		self._regB = []
		self._regP = []
		self._active = False
		self._duration = 1
		self._last = False

	def __str__(self):
		
		if not self.is_empty():
			regA = list(self._regA)
			regA.reverse()
			regB = list(self._regB)
			regB.reverse()
			regP = list(self._regP)
			regP.reverse()
			return "A: " + " ".join(str(value) for value in regA) + \
				" " + "B: " +  " ".join(str(value) for value in regB) + \
				" " + "P: " +  " ".join(str(value) for value in regP) + \
				" " + str(self._active)
		else:
			return "Empty" + " " + str(self._active)

	def load(self, divident, divider, temp_remainder):
		"""
		loads numbers into processing unit
		"""
		self._regA = list(divident)
		self._regB = list(divider)
		self._regP = list(temp_remainder)

	def reset(self):
		"""
		resets all unit's parameters
		"""
		self._regA = []
		self._regB = []
		self._regP = []
		self._active = False

	def shift(self):
		"""
		performs shift of pair <regP, regA>
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
			self._regP = list(self.subtract(self._regP, self._regB))
		else:
			self.shift()
			self._regP = list(self.add(self._regP, self._regB))

		if self.is_regP_positive():
			self._regA.insert(0, 1)
		else:
			self._regA.insert(0, 0)

		if self._last:
			if not self.is_regP_positive():
				self._regP = list(self.add(self._regP, self._regB))

	def get_regP(self):
		return self._regP

	def get_regA(self):
		return self._regA

	def get_regB(self):
		return self._regB

	def is_empty(self):
		return not (len(self._regA) > 0 and len(self._regP) > 0)

	def last(self, value):
		self._last = value

	def get_duration(self):
		return self._duration

	def set_duration(self, value):
		self._duration = value

	def active(self, value):
		self._active = value

	def is_active(self):
		return self._active


