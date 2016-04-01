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
infile = open('wind_sites.csv','rb')	# opens the csv file
# save the results of the .csv to a variable
reader = csv.reader(infile)

# initialize variables that will change within the loop
WS80      = -9999
WS80_temp = -9999
ID80      = -9999
# initialize for additional heights
firstRow  = True

# read each row of code
for row in reader:
	if firstRow:
		firstRow = False
	else:
		# read in and save each element
		siteID = row[0]
		# continue for the rest of the variables
		MH1 = row[1]
		# ...

		# call shear_calc function
		WS80_temp = shear_calc(MH1,WS1,MH2,WS2,80)
		WS100_temp = shear_calc(MH1,WS1,MH2,WS2,100)
		# call function for additional heights
		# ...

		# check if it is the fastest windspeed
		# if so, save it
		# if not, continue to next row
		if WS80_temp > WS80:
			WS80 = WS80_temp	# save out the windspeed
			ID80 = siteID		# save out the siteID
		# check additioanl heights
		# ...

# now create the file that we will write to
outfile = csv.writer(open('wind_summary.csv', 'wb'))
outfile.writerow(['DesiredHeight','windiestSiteNumber','windSpeed'])
outfile.writerow([80,ID80,WS80])
# keep doing this for other hub heights

# save and close the infile


# if you have time try to imbed the repeated processes within loops