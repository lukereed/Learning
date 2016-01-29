#!/usr/bin/python

# Luke Reed
# ex04.py
# 01/07/2016
# Variables and Names

cars                        = 100 # integer
space_in_a_car              = 4.0 # floating point
drivers                     = 30 # integer
passengers                  = 90. # floating point
cars_not_driven             = cars - drivers
cars_driven                 = drivers
carpool_capacity            = cars_driven * space_in_a_car
average_passengers_per_car  = passengers / cars

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "total passengers"
print "We need to put about", average_passengers_per_car, "in each car"
