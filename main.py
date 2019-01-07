import listdir
import os, sys
from createImg import createImg

try:
	if len(sys.argv) == 1:
		raise BaseException(input('Podaj nazwę pliku lub folderu: '))

	if os.path.exists(sys.argv[1]): files = listdir.listdir(sys.argv[1])
	else: raise f'The {sys.argv[1]} path doesn\'t exist'
	name = sys.argv[1]
except BaseException as err:
	name = str(err)

print('Analizowanie struktury folderu')
files = listdir.listdir(name)
files = listdir.flattenDict(files)
files = listdir.flatten(files)
files = listdir.excludeType(files)

img = createImg()

for path in files:
	img.addFile(path)

print('Generowanie obrazu')
img.commit()
img.save('image.jpg')
img.img.show()
os.system('pause')