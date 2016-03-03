# Luke Reed
# IntegerErrorHandling.py
# 03/03/2016

while True:

	try:
		n = raw_input("Please enter an integer: ")
		n = int(n)
		break

	except ValueError:
		print("Not a valid integer! Please try again ...")

print("Great, you successfully entered an integer!")