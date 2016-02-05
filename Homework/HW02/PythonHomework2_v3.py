#!/usr/bin/python

"""
Homework #2

Create a python script which will read in the accompanying
file wind_sites.csv and for each of 80m, 100m and 120m as the
desired height (DH) find which site in the accompanying file
is the windiest.

You should use the method/function you created last week to 
run through the calculation of wind speed for each site/DH option.

The output of your script should be a new, separate file
which has the columns: DesiredHeight, windiestSiteNumber, windSpeed

where:
DesiredHeight - the three options of 80, 100 and 120
windiestSiteNumber - The site number corresponding to the windiest
					 site for that desired height
windSpeed - the speed of the windiest site, at the desired height

"""

# first import libraries
import math
import numpy as np
import sys
import csv	# imports the csv module

# define script inputs
#script, fname = sys.argv

# define shear calcualtion function
def shear_calc(MH1, WS1, MH2, WS2, DH):
	# first make sure all variables are floats not integers/strings
	MH1 = float(MH1)
	WS1 = float(WS1)
	MH2 = float(MH2)
	WS2 = float(WS2)
	DH  = float(DH)
	# now we can determine our shear exponent and wind speed
	# ln = math.log and log_{10} = math.log10
	shear_exp = math.log(WS1 / WS2) / math.log(MH1 / MH2)
	wind_speed = WS2 * (DH / MH2) ** shear_exp
	# return the wind speed value
	return wind_speed

# now read in the .csv
infile = open('wind_sites.csv','rb')	# opens the csv file
numlines = len(infile.readlines())	# counts the number of lines in the .csv

# read in the file again since it was closed out above
infile = open(sys.argv[1],'rb')	# opens the csv file
reader = csv.reader(infile)

# initialize variables
DH = [80,100,120]
DH_len = len(DH)	# records the length of DH
SiteNumber = [-9999] * DH_len
windSpeed  = [-9999] * DH_len
tempspeed  = [-9999] * DH_len
full_array = np.ones((numlines-1,(5+DH_len))) * -9999
rownum = 0

# now loop through each line
firstline = True	# boolean variable to skip first line
for row in reader:
	if firstline:
		firstline = False	# turn off header variable
	else:
		# save all values into an array
		for ii in range(0,DH_len+5):
			# input values
			if ii < 5:
				full_array[rownum,ii] = row[ii]
			# calculated DH windspeeds
			else:
				full_array[rownum,ii] = shear_calc(row[1],row[2],row[3],row[4],DH[ii-5])
		rownum += 1

# now find the index of the max value for each of the DH's and extract values
for ii in range(0,DH_len):
	index = np.argmax(full_array[:,ii+5])
	SiteNumber[ii] = full_array[index,0]
	windSpeed[ii] = full_array[index,ii+5]

# now create the file that we will write to
outfile = csv.writer(open('wind_summary.csv', 'wb'))
outfile.writerow(['DesiredHeight','windiestSiteNumber','windSpeed'])
# Loop through the number of DH values and write each to a row
for i in range(0,DH_len):
	outfile.writerow([DH[i], SiteNumber[i], windSpeed[i]])

# save and close the file
infile.close()
