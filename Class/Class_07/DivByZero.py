# Luke Reed
# DivByZero.py
# 03/03/2016

# Don't try to capture every single error, but make sure that the major/common
# ones are covered

import sys

first_number = raw_input("Enter the first number: ")
second_number = raw_input("Enter the second number: ")

firstNumber = float(first_number)
secondNumber = float(second_number)

try:			# this allows us to try a code block
	result = firstNumber / secondNumber
	print first_number + '/' + second_number + ' = ' + str(result)

except ZeroDivisionError:	# if the first code block doesn't work, we go to the 'except'
	print("The answer is infinity")
	sys.exit()

except:			# execution information captures error message
	error = sys.exc_info()[0]
	print("Sorry, there was some other error")
	print(error)
	# this code block will be triggered if we have a typo else where
	# changing the '+' to a '-' in the print statement

# the difference between printing at the end and using 'finally' is that
# 'finally' keeps it within the code block 
finally:		# this block will always run
	print("Code in this section will always run")