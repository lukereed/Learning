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
#infile = open(sys.argv[1],'rb')	# opens the csv file
infile = open('wind_sites.csv','rb')	# opens the csv file

# save the results of the .csv to a variable
numline = len(infile.readlines())	# counts the number of lines in the .csv
reader = csv.reader(infile)
print 'numline = ', numline

# initialize variables
DH = [80,100,120]
DH_len = len(DH)	# records the length of DH
SiteNumber = [-9999] * DH_len
windSpeed  = [-9999] * DH_len
tempspeed  = [-9999] * DH_len
#full_array = [x[:] for x in [[-9999]*(5+DH_len)]*numline]
full_array = np.ones((numline,(5+DH_len))) * -9999

#print full_array

# now loop through each line
rownum = 0			# index of what row is being worked on
firstline = True	# boolean variable to skip first line
for row in reader:
	if firstline:
		firstline = False	# turn off header variable
		rownum += 1
	else:
		ID  = row[0]
		print 'ID = ', ID
		MH1 = row[1]
		WS1 = row[2]
		MH2 = row[3]
		WS2 = row[4]

		full_array[rownum,0] = ID
		full_array[rownum,1] = MH1
		full_array[rownum,2] = WS1
		full_array[rownum,3] = MH2
		full_array[rownum,4] = WS2


		# loop through each of the DH values
		for ii in range(0,DH_len):
			# for each DH value, compute the shear calc
			tempspeed[ii]  = shear_calc(MH1,WS1,MH2,WS2,DH[ii])
			full_array[rownum,ii+5]  = shear_calc(MH1,WS1,MH2,WS2,DH[ii])
			# now check to see if it is the highest windspeed
			# if so, save the speed and site number
#			if tempspeed[ii] > windSpeed[ii]:
#				windSpeed[ii]  = tempspeed[ii]
#				SiteNumber[ii] = ID

		rownum += 1
print 'rownum = ', rownum
print 'firstline = ', firstline
#print full_array
'''
# now create the file that we will write to
outfile = csv.writer(open('wind_summary.csv', 'wb'))
outfile.writerow(['DesiredHeight','windiestSiteNumber','windSpeed'])
# Loop through the number of DH values and write each to a row
for i in range(0,DH_len):
	outfile.writerow([DH[i], SiteNumber[i], windSpeed[i]])
# save and close the file '''
infile.close()