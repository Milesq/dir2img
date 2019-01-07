from os import listdir as ls
from os.path import isdir, join

def listdir(path='./'):
	ret = {}
	for i in ls(path):
		absPath = join(path, i)
		if isdir(absPath):
			ret[absPath] = listdir(absPath)
		else:
			ret[absPath] = None

	return ret

def flatten(l):
	for i in l:
		if type(i) == type([]):
			for j in flatten(i): yield j
		else: yield i

def flattenDict(obj):
	ret = [x for x in obj]
	for i in obj:
		if obj[i] != None:
			ret.append(flattenDict(obj[i]))
	return ret
def excludeType(list, directory=True):
	for i in list:
		if directory != isdir(i):
			yield i