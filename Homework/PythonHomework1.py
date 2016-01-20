"""
Homework for 1/6/2016

Create a python script which will calculate the
wind speed at a specified height with the inputs:
1.) Measurement Height 1 (MH1)
2.) Wind speed at measurement height 1 (WS1)
3.) Measurement Height 2 (MH2)
4.) Wind speed at measurement height 2 (WS2)
5.) Height at which you want the wind speed (DH)

Use sys.argv so that the script can be run in the
following manner:
$ python PythonHomework1.py MH1 WS1 MH2 WS2 DH

Which will end up printing:
$ The wind speed at 80m is 9.8m/s

The calculation should be inside a function/method.

For those not in the wind group, the calculation
is as follows:
shear_exponent = ln(WS1 / WS2) / ln(MH1 / MH2)
wind_speed = WS2 * (DH / MH2) ^ shear_exponent

"""

# Luke Reed
# PythonHomework1.py
# 01/16/2015
# A script to calculate wind speed at a specified height

# import necessary libraries
import sys
import math

# define inputs
script, MH1, WS1, MH2, WS2, DH = sys.argv

# begin function
def shear_calc(MH1, WS1, MH2, WS2, DH):
	# first make sure all variables are floats not integers/strings
	MH1 = float(MH1)
	WS1 = float(WS1)
	MH2 = float(MH2)
	WS2 = float(WS2)
	DH  = float(DH)
	# now we can determine our shear exponent and wind speed
	shear_exp = math.log(WS1 / WS2) / math.log(MH1 / MH2)
	wind_speed = WS2 * (DH / MH2) ** shear_exp
	# return the wind speed value
	return wind_speed

# call the funciton and save out the returned value
wind_speed = shear_calc(MH1, WS1, MH2, WS2, DH)

# now print out the desired result
print "The wind speed at %sm is %rm/s" % (DH,wind_speed)

# QUESTIONS
# Why does sys.argv automatically input information as strings?

