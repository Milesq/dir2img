import listdir
import os, sys
from createImg import createImg

os.system('cls')

if os.path.exists(sys.argv[1]): files = listdir.listdir(sys.argv[1])
else: raise f'The {sys.argv[1]} path doesn\'t exist'

files = listdir.listdir(sys.argv[1])
files = listdir.flattenDict(files)
files = listdir.flatten(files)

img = createImg()

for path in files:
	img.addFile(path)

img.commit()
# img.save('image.jpg')
# img.img.show()