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