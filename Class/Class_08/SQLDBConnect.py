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

	# # try:
	# # 	myCursor = myConnection.cursor()
	# # 	# SQLSelectCommand = ("Select custname, city FROM Customers WHERE custnum = '20042'")
	# # 	SQLSelectCommand = ("Select custname, city FROM Customers WHERE custnum = ?")
	# # 	Value = ['20042']
    # #
	# # 	# myCursor.execute(SQLSelectCommand)
	# # 	myCursor.execute(SQLSelectCommand, Value)
    # #
	# # 	myResult = myCursor.fetchone()		# stores all results 1 by 1 in an array
	# # 	print"Customer Name = " + myResult[0]
	# # 	print "City Name = " + myResult[1]
    #
	# except:
	# 	print("SQL SELECT command failed")
	# 	# myConnection.commit()
	# 	myConnection.close()

	# try:
	# 	myCursor = myConnection.cursor()
	# 	# SQLSelectCommand = ("SELECT * FROM Customers")
	# 	SQLSelectCommand = ("SELECT RTRIM(CAST(custname AS VARCHAR)) AS custname, RTRIM(CAST(city AS VARCHAR)) AS city FROM Customers")
    #
	# 	myCursor.execute(SQLSelectCommand)
    #
	# 	# rows = myCursor.fetchall()
	# 	# print(str(rows))
    #
	# 	# myResult = myCursor.fetchone()
	# 	# while myResult is not NONE:
	# 	# 	print(myResult)
	# 	# 	myResult = myCursor.fetchone()
	# 	for row in myCursor:
	# 		print(row)
    #
	# except:
	# 	print("SQL SELECT command failed")
	# 	# myConnection.commit()
	# 	myConnection.close()

	try:
		myCursor = myConnection.cursor()
		# SQLSelectCommand = ("SELECT * FROM Customers")
		SQLSelectCommand = ("SELECT * FROM Customers")

		myCursor.execute(SQLSelectCommand)

		one_row = myCursor.fetchone()
		two_rows = myCursor.fetchmany(num=2)
		remaining_rows = myCursor.fetchall()
		print(one_row)
		print(two_rows)
		print(remaining_rows)

	except:
		print("SQL SELECT command failed")
		# myConnection.commit()
		myConnection.close()

	# try:
	# 	myCursor = myConnection.cursor()
    #
	# 	SQLInsertCommand = ("INSERT INTO Cars "
	# 					   "(CarID,CarMake,CarModel) "
	# 					   # "VALUES('?','?','?')")			# we could alternatively insert values directly into the SQL command
	# 					   "VALUES('C06','Tesla','S3')")			# we could alternatively insert values directly into the SQL command
	# 	VALUES = ['C06','Tesla','S3']
    #
	# 	#myCursor.execute(SQLSelectCommand)
	# 	myCursor.execute(SQLInsertCommand)
    #
	# 	myConnection.commit()
	# 	print("Inserted Successfully")
    #
	# except:
	# 	print("SQL Insert command failed")
	# 	myConnection.commit()
	# 	myConnection.close()

except:
	print("could not connect")
	error = sys.exc_info()
	print(error)
	sys.exit()

finally:
	print("closing DB connection")
	myConnection.close()