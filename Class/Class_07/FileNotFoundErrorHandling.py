# Luke Reed
# FileNotFoundErrorHandling.py
# 03/03/2016
# A script to handle errors when trying to load a file that is not there

import sys

fname = raw_input("Filename: ")

try:
#`	newfile = open('SimpleTextFile.txt')
	myFile = open(fname, "r")
	fileFound = True

except IOError:
	print('The file doesn\'t exit!')
	fileFound = False

except:
	print("Found file" + fname + " but some other error")
	error - sys.exc_info()
	print(error)
	fileFound = False

if fileFound:
	fileContents = myFile.read()
	print(fileContents)