from PIL import Image
import os

class createImg:
	def __init__(self):
		self.size = 0
		self.img = Image.new('RGB', (8192, 8192), 'white')
		self.files = []

		self.x = 0
		self.y = 0

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
		self.img = Image.new('RGB', (self.size, self.size), 'white')
		pixs = self.img.load()

		for i in self.files:
			fileSize = int((os.path.getsize(i) % 8192) / 3)
			content = createImg.getFile(i)
			
			j = 0
			for i in range(fileSize):
				rgb = (content[j:j+3])
				print(rgb)
				rgb = ((x+1 % 255) - 1 for x in rgb)
				j += 3
				# pixs[self.next] = rgb