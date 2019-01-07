from PIL import Image
import os

class createImg:
	def __init__(self):
		self.size = 0
		self.img = Image.new('RGB', (8192, 8192), 'white')
		self.files = []

	@staticmethod
	def getFile(pathToFile):
		f = open(pathToFile, 'rb')
		content = f.read()
		f.close()
		return content

	def save(self, name):
		self.img.save(name, 'JPEG')

	def addFile(self, path):
		self.size += os.path.getsize(path)
		self.files.append(path)

	def commit(self): pass
		# self.size = int(self.size % 8192)
		# self.img = Image.new('RGB', (self.size, self.size), 'white')
		# pixs = self.img.load()

		# for el in self.files:
		# 	content = createImg.getFile(el)
		# 	print(content[0])