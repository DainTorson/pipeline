
class FileReader():
	"""
	reads file and process data
	"""

	def __init__(self):

		self.file = None

	def set_file(self, path):
		"""
		sets target file
		"""

		self.file = open(path) 

	def read(self):
		"""
		reads file, returns input data list
		"""

		result = []
		if self.file != None:
			for line in self.file:
				temp = line.split(" ")
				if len(temp) < 2:
					return []
				else:
					result.append((int(temp[0]), int(temp[1])))
		return result
