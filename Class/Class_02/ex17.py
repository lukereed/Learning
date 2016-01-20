# Luke Reed
# ex17.py
# 01/14/2016
# More Files
# This script will copy one file to another

from sys import argv
# import exists from the operating system
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# open and read the 'in_file'
in_file = open(from_file)
indata  = in_file.read()

# alternatively we could do this in a single line
# indata  = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

# use 'exists' function from os.path library
print "Does the output file exist? %r" % exists(to_file)
print "Read, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# close the files (save)
out_file.close()
in_file.close() # if we opened and read the file in a single line we don't need this line