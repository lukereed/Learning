# Luke Reed
# SQLDBConnect.py
# 03/10/2016

import sys
import pypyodbc

print ("try to connnect to DB... ")

try:
	myConnection = pypyodbc.connect('DRIVER={SQL Server};'
									'SERVER=.\SQLEXPRESS;'
									'DATABASE=FullerAckerman;'
									'UID=sa;PWD=Password01')
	print("connected to DB")

except:
	print("could not connect")
	error = sys.exc_info()
	print(error)
	sys.exit()

finally:
	print("closing DB connection")
	myConnection.close()