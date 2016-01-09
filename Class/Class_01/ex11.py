# Luke Reed
# ex11.py
# 01/07/2016
# Asking Questions

# Take some kind of input from a person
# Print out something
print "What is your name?",
name = raw_input()      # this allows the user to enter data
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy" % (age, height, weight)
