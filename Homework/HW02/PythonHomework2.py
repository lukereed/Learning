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
infile = open(sys.argv[1],'rb')	# opens the csv file

# save the results of the .csv to a variable
reader = csv.reader(infile)
firstline = True	# boolean variable to skip headers

# initialize variables
SiteNumber80  = -999
SiteNumber100 = -999
SiteNumber120 = -999
windSpeed80   = -999
windSpeed100  = -999
windSpeed120  = -999
# now loop through each line
for row in reader:
	if firstline:
		firstline = False	# turn off header variable
	else:
		ID  = row[0]
		MH1 = row[1]
		WS1 = row[2]
		MH2 = row[3]
		WS2 = row[4]

		tempspeed_80  = shear_calc(MH1,WS1,MH2,WS2,80)
		tempspeed_100 = shear_calc(MH1,WS1,MH2,WS2,100)
		tempspeed_120 = shear_calc(MH1,WS1,MH2,WS2,120)

		# now check to see if it is the highest windspeed
		if tempspeed_80 > windSpeed80:
			windSpeed80  = tempspeed_80
			SiteNumber80 = ID
		if tempspeed_100 > windSpeed100:
			windSpeed100  = tempspeed_100
			SiteNumber100 = ID
		if tempspeed_120 > windSpeed80:
			windSpeed120  = tempspeed_120
			SiteNumber120 = ID
		
# now create the file that we will write to
outfile = csv.writer(open('wind_summary.csv', 'wb'))
outfile.writerow(['DesiredHeight','windiestSiteNumber','windSpeed'])
outfile.writerow([80, SiteNumber80, windSpeed80])
outfile.writerow([100,SiteNumber100,windSpeed100])
outfile.writerow([120,SiteNumber120,windSpeed120])

# save and close the file
infile.close()