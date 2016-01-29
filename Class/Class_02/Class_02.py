#!/usr/bin/python

# Luke Reed
# Class 02
# 01/14/2016

# Homework01 Review
# uncomment each section individually to make it executable
# One possible solution
'''
import math
from sys import argv
script, MH1, WS1, MH2, WS2, DH = argv

def windspeed(MH1,WS1,MH2,WS2,DH):
	shear_exponent = (math.log(float(WS1)/float(WS2)) / (math.log(float(MH1)/float(MH2)))
	wind_speed = float(WS2) * (float(DH)/float(MH2)) ** shear_exponent

	print "The wind speed at", DH, "m is", wind_speed, "m/s"
	print "The wind speed at %sm is %sm/s" % (str(DH),str(wind_speed))
	print "The wind speed at %.2fm is %.2fm/s" % (float(DH),float(wind_speed))

windspeed(MH1,WS1,MH2,WS2,DH)
'''

'''
# Alternatively we could do this using raw input
import math
MH1 = raw_input("Measurement Height 1: ")
MH2 = raw_input("Measurement Height 2: ")
WS1 = raw_input("Wind speed at Measurment Height 1: ")
WS2 = raw_input("Wind speed at Measurment Height 2: ")
DH  = raw_input("Height at which you want the wind speed: ")

print MH1, WS1, MH2, WS2, DH

# same function as before
# recall that 'ln' --> math.log and 'log' --> math.log10
def windspeed(MH1,WS1,MH2,WS2,DH):
	shear_exponent = (math.log(float(WS1)/float(WS2))) / (math.log(float(MH1)/float(MH2)))
	wind_speed = float(WS2) * (float(DH)/float(MH2)) ** shear_exponent

	print "The wind speed at", DH, "m is", wind_speed, "m/s"
	print "The wind speed at %sm is %sm/s" % (str(DH),str(wind_speed))
	print "The wind speed at %.2fm is %.2fm/s" % (float(DH),float(wind_speed))

windspeed(MH1,WS1,MH2,WS2,DH)
'''

'''
# We can introduce reading/writing files
fil = open("foo.txt", "w")	# opens a file in 'write' mode

print "Name of the file: ", fil.name
print "Closed or not : ", fil.closed
print "Opening mode :", fil.mode

# now write to the file
fil.write("Hello")
fil.write("\n")
fil.write("Hello There")
fil.close()	# closes the file for writing

# open the file for reading
file = open("foo.txt", 'r')
print file.read() + " World"
print file.readline()	# reads line by line
print file.readline()

fil.close() 	# close (save) the file when done
'''


# A final modification to the homework program by reading inputs from a file
from sys import argv
import math

script, filename = argv

# open the file
fil = open(filename, "r")
# read and store the values line by line
MH1 = fil.readline()
WS1 = fil.readline()
MH2 = fil.readline()
WS2 = fil.readline()
DH  = fil.readline()

def windspeed(MH1,WS1,MH2,WS2,DH):
	shear_exponent = (math.log(float(WS1))/float(WS2)) / (math.log(float(MH1)/float(MH2)))
	wind_speed = float(WS2) * (float(DH)/float(MH2)) ** shear_exponent

	print "The wind speed at", DH, "m is", wind_speed, "m/s"
	print "The wind speed at %sm is %sm/s" % (str(DH),str(wind_speed))
	print "The wind speed at %.2fm is %.2fm/s" % (float(DH),float(wind_speed))

windspeed(MH1,WS1,MH2,WS2,DH)

