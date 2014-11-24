import os

files = os.listdir(os.getcwd())
for f in files:
	print "%s" %f
