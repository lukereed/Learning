# Luke Reed
# ex16.py
# 01/14/2016
# Reading and Writing Files

from sys import argv

script, filename = argv

# close --> closes the file (Like File->Save)
# read --> Reads the contents of the file
# readline --> Reads just one line of a text file
# truncate --> Empties the file. Watch out if you care about the file
# write('stuff') --> Writes 'stuff' to the file

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# open the file in writing mode
print "Opening the file..."
target = open(filename, 'w')	# 'w' opens it in writing mode

# truncate the file (erase)
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write the three different lines to the file on a new line each time
# target is the object that is being written to
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# close the file (save)
print "And finally, we close it."
target.close()