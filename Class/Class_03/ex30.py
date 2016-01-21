# Luke Reed
# ex30.py
# Else and If
# An exercise to show what happens if a conditional statement isn't satisfied

people = 30
cars = 40
trucks = 15


# initial if statement
if cars > people:
	print "We should take the cars."
# secondary if statement if the first is not satisfied
elif cars < people:
	print "We should not take the cars."
# catch all if the prior conditionals are not satisfied
else:
	print "We can't decide."


if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."


if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."