#!/usr/bin/python

# Luke Reed
# Class_02.py
# 01/21/2016

# import required libraries
import math 

# Homework_01 Extension
fil = open("windspeed_inputs.txt", "r")

# open the file
fil = open("windspeed_inputs.txt", "r")
# read and store the values line by line
MH1 = float(fil.readline())
WS1 = float(fil.readline())
MH2 = float(fil.readline())
WS2 = float(fil.readline())
DH  = float(fil.readline())

print MH1, WS1, MH2, WS2, DH

def calc_wind_speed(MH1,WS1,MH2,WS2,DH):
	shear_exponent = (math.log(float(WS1))/float(WS2)) / (math.log(float(MH1)/float(MH2)))
	wind_speed = float(WS2) * (float(DH)/float(MH2)) ** shear_exponent

	print "The wind speed at", DH, "m is", wind_speed, "m/s"
	print "The wind speed at %sm is %sm/s" % (str(DH),str(wind_speed))
	print "The wind speed at %.2fm is %.2fm/s" % (float(DH),float(wind_speed))

calc_wind_speed(MH1,WS1,MH2,WS2,DH)

########################################################################

'''
Class outline topics

- Boolean logic
	ex29.py		What If
	ex30.py		Else and If
	ex31.py		Making Decisions - "Choose your own adventure"
- Loops
	ex32.py		Loops and Lists
	ex33.py 	While Loops
- Lists
	Accessing elements of Lists
		note: python starts with the 0th element when indexing lists
'''

temp = int(raw_input("Enter the temperature: "))
if temp < 76:
	print "Don't go swimming!"

num = int(raw_input("Enter a number: "))
if num > 1000000:
	print num, "is a big number."
else:
	print "your number is", num

hour = int(raw_input("Enter the hour: "))
if hour < 12:
	print "Good morning"
# note that we don't have to say '> 12' because it has been
# filtered out with the previous line
elif hour < 18:
	print "Good afternoon"
elif hour < 23:
	print "Good evening"
else:
	print "You're up late"

# Now we can introduce For and While Loops
# initialize our count
count = 0
while count < 9:	# this loop will continue until this condition is no longer met
	print count		# this will print the numbers 0 through 8
	count += 1 		# increase the number by 1

# first value in range function is starting value/index
# second value is the number of elements to loop go through
for x in range(0,10):
	print x			# this will print the numbers 1 through 9

# this will loop through each element in the string
for x in "python":
	print x			# prints "python" letter by letter

# now let's look at list indexing
animals = ['bear','tiger','elephant']
print animals[2] # this prints elephant (index starts at zero)



##########################################################################

# Homework_02 Outline/Start
fil = open('wind_sites.csv', 'r')

for line in fil:
	print line
	test = line.split(',')	# this will split the string by ','

print test[2] # this will print the third element in the last row of the .csv

fil.close()

