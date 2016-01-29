#!/usr/bin/python

# Luke Reed
# RES Python Class 01
# 01/07/2016


# Classic "hello world" welcome to programming
print "Hello World!"
print "Hello Again!"

# We can now learn about different types
type(55)        # this will return 'int' for integers
type(55.34)     # this will return 'float' for floating points
type(55)        # this will also return 'float' for floating points
type('text')    # this will return 'str' for character strings

# Now how about some numerical operations
print 59/60     # will return '0' because of integer math
print 59/60.    # will return '0.983333333333'

# Next we can combine text and numerical operations
print 'here is some math:', 36+5./2

# EXERCISES!
# 1. Math Operations
#    If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile?
#    What is your average speed in miles per hour? (Hint: there are about 1.61 kilometers in a mile.)
D = 10
m = 43
s = 30
miles = 10 / 1.61
time = (43 + 30 / 60.) / 60.   # time in hours
pace = time / miles * 60
mph = miles / time
print "Average time per mile: ", pace, "minutes"
print "Average speed (mph): ", mph


# 2. The volume of a sphere with radius r is 4/3 pi r3. What is the volume of a sphere with radius 5?
#    first load up math library
import math         # import entire math library
#from math import pi # alternative way to just import part of a library
r = 5
volume = 4./3 * math.pi ** 3
print "The volume of a sphere with radius %d is %f" % (r,volume)


# 3. If I leave my house at 6:52AM and run 1 mile at an easy pace (8:15 per mile), then 3 miles at temp (7:12 per mile)
#    and 1 mile at an easy pace again, what time do I get home for breakfast?
start_time = (6*60 + 52) * 60
easy_pace  = 8*60 + 15
tempo      = 7*60 + 12
run_time   = easy_pace + 3*tempo + easy_pace
end_time   = start_time + run_time
end_hour   = end_time / 60 / 60
end_minute = (end_time - (end_hour*60*60) ) / 60
end_second = (end_time - (end_hour*60*60) - (end_minute*60))
print "Breakfast will be at %d:%d:%d" % (end_hour,end_minute,end_second)


# 4. Functions
#    Python provides a built-in function called len that returns the length of a string, so the value of len("allen") is 5.
#    Write a function named right_justify that takes a string named 's' as a parameter and prints the string with enough
#    leading spaces so that the last letter of the string is in column 70 of the display

s = raw_input("Give me a string:\n>")   # begin with asking for input from the user
def right_justify(s):                   # define a function
    l = len(s)                          # determine the length of the inputted string
    print (' '*(70-l)+s)                # use the ' ' for blank space and the + to concatenate the string
# execute the function on the inputted string
right_justify(s)
    
