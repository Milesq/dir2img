from PIL import Image
from math import sqrt
import os

class createImg:
	def __init__(self):
		self.size = 0
		self.img = Image.new('RGB', (8192, 8192), 'white')
		self.files = []

		self.x = 0
		self.y = 0

	def next(self):
		if self.y >= self.size-1:
			return (0, 0)
		if self.x >= self.size-1:
			self.x = 0
			self.y += 1
		else: self.x += 1
		return (self.x, self.y)

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

	def commit(self):
		self.size = int((self.size % 8192) / 3)
		self.size = int(sqrt(self.size)) + 1
		self.img = Image.new('RGB', (self.size, self.size), 'white')
		pixs = self.img.load()

		for i in self.files:
			print(f'Przetwarzanie {i}')
			fileSize = int((os.path.getsize(i) % 8192) / 3)
			content = createImg.getFile(i)
			
			j = 0
			for i in range(fileSize):
				rgb = (content[j:j+3])
				rgb = tuple(((x+1 % 255) - 1 for x in rgb))
				j += 3
				pixs[self.next()] = rgb