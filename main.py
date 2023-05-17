#VEHICLE MANAGEMENT SYSTEM

import mysql.connector as sql

def Bus_Management(cursor, database):
	#Inserting into Bus Management
	def insertBus(cursor, database):
		while True:
			print("Enter the details following...")
			busID = input("BUSID : ")
			type = input("AC or NON-AC : ")
			manufacturer = input("Bus manufacturer : ")
			vehicleNumber = input("Registered Vehicle Number : ")
			fuelConsumed = float(input("Fuel used (in Litres): "))
			capacity = int(input("Seats Capacity : "))
			mileage = float(input("Mileage of vehicle per litre (in kms) : "))
			serviceDate = input("Date of last service done (YYYY-MM-DD) : ")
			query = f"INSERT INTO BUS_MANAGEMENT VALUES('{busID}','{type}','{manufacturer}','{vehicleNumber}',{fuelConsumed},{capacity},{mileage},'{serviceDate}')"
			cursor.execute(query)
			database.commit()
			choice = input("Want to insert more details(y/n) : ")
			if choice.lower() != 'y':
				break	

	#updating Bus Management
	def updateBus(cursor, database):
		print("Enter the details following...")
		busID = input("Enter the BusId to update : ")
		type = input("AC or NON-AC : ")
		manufacturer = input("Updated Bus Manufacturer : ")
		vehicleNumber = input("Updated Registered Vehicle Number : ")
		fuelConsumed = float(input("Updated Fuel consumed (in litres) : "))
		capacity = int(input("Updated Seats Capacity : "))
		mileage = float(input("Updated Mileage of vehicle per litre (in kms) : "))
		serviceDate = input("Updated date of service done(YYYY-MM-DD) : ")
		query = f"UPDATE BUS_MANAGEMENT SET TYPE='{type}',MANUFACTURER='{manufacturer}',REGISTERED_NO='{vehicleNumber}',FUEL={fuelConsumed},SEATS_CAPACITY={capacity},MILEAGE={mileage},LAST_SERVICE_DONE='{serviceDate}' WHERE BUS_ID='{busID}'"
		cursor.execute(query)
		database.commit()
		print('DONE!!')

	#deleting in bus management
	def deleteBus(cursor, database):
		busID = input("Enter the Bus id to delete the details : ")
		query = f"DELETE FROM BUS_MANAGEMENT WHERE BUS_ID='{busID}'"
		cursor.execute(query)
		database.commit()

	#showing details of Bus Management
	def fetchBus(cursor, database):
		print("You can now view the bus details!")
		choice = input("Wish to see the whole data (y/n) : ")
		if choice.lower() == 'y':
			query = "SELECT * FROM BUS_MANAGEMENT"
			cursor.execute(query)
			details = cursor.fetchall()
			for detail in details:
				print(detail)
		else:
			print("You can view a single record at a time!")
			while True:
				busID = input("Enter the Bus ID : ")
				query = f"SELECT * FROM BUS_MANAGEMENT WHERE BUS_ID='{busID}'"
				cursor.execute(query)
				print(f"{busID} :\n",cursor.fetchone())
				print("You can view more Bus details!!")
				choice = input("Want to Continue (y/n) : ")
				if choice.lower() != 'y':
					break

	#_main_Bus Management
	print("Welcome to the Bus Management module.")
	print("NOTE: If any details are unknown to you then skip it or type NULL except for the Bus Id, Fuel, Mileage and Seat, which are must.")
	
	while True:
		print("Select\n1. Upload Details\n2. Update details\n3. Delete details\n4. View Details\n5. Exit Module")
		choice = input("Your choice : ")
		if choice == '1':
			insertBus(cursor, database)
		elif choice == '2':
			updateBus(cursor, database)
		elif choice == '3':
			deleteBus(cursor, database)
		elif choice == '4':
			fetchBus(cursor, database)
		elif choice == '5':
			break
		else:
			print("Sorry, the operation you are in search of doesnot exist or in implementation!")
	#end of Bus Management

	
def Route_Management(cursor, database):
	#inserting into ROUTE MANAGEMENT
	def insertRoute(cursor, database):
		print("You can now Add Data!")
		while True:
			print("Enter the details following...")
			routeId = input("Route ID : ")
			boardingPalce = input("Place of Boarding : ")
			destinationPlace = input("Place of Destination : ")
			cities = input("Cities in between the route (seperated by comma) : ")
			busID = input("Dedicated Bus ID for the route : ")
			estimatedTime = input("Estimated duration of journey (in hours): ")
			capacity = int(input("Seats Available : "))
			trips = int(input("Number of trips per day : "))
			query = f"INSERT INTO ROUTE_MANAGEMENT VALUES('{routeId}','{boardingPalce}','{destinationPlace}','{cities}','{busID}','{estimatedTime}',{trips},{capacity})"
			cursor.execute(query)
			database.commit()
			choice = input("Want to insert more data (y/n) : ")
			if choice.lower() != 'y':
				break		

	#Updating Route Management
	def updateRoute(cursor, database):
		print("You can now Update!\nEnter the details following...")
		routeID = input("Bus ID to be update : ")
		boardingPlace = input("Updated Place of Boarding : ")
		destinationPlace = input("Updated Place of Destination : ")
		cities = input("Updated cities in between the Route (seperated by comma) : ")
		busID = input("Updated Dedicated Bus Id for the route : ")
		estimatedTime = input("Updated estimated duration of journey(in hours) : ")
		capacity = int(input("Updated Seats Available : "))
		trips = int(input("Updated number of trips per days : "))
		query = f"UPDATE ROUTE_MANAGEMENT SET PLACE_OF_BOARDING='{boardingPlace}',PLACE_OF_DESTINATION='{destinationPlace}',CITIES_IN_BETWEEN='{cities}',DEDICATED_BUSID='{busID}',DURATION='{estimatedTime}',TRIPS_PER_DAY={trips},AVAILABLE_SEATS={capacity} WHERE ROUTE_ID='{routeID}'"
		cursor.execute(query)
		database.commit()
		print('DONE!!')	

	#Delete from Route Management
	def deleteRoute(cursor, database):
		print("You can now Delete any record!")
		routeID = input("Enter the Route ID to be deleted : ")
		query = f"DELETE FROM ROUTE_MANAGEMENT WHERE ROUTE_ID='{routeID}'"
		cursor.execute(query)
		database.commit()
		print("Done!")
	
	#viewing deatils of Route Management
	def fetchRoute(cursor, database):
		print("You can now view details!")
		choice = input("Wish to view the whole data (y/n) : ")
		if choice.lower() == 'y':
			query = "SELECT * FROM ROUTE_MANAGEMENT"
			cursor.execute(query)
			details = cursor.fetchall()
			print("The Route details are:")
			for detail in details:
				print(detail)
		else:
			print("Can view single record at a time!")
			while True:
				routeID = input("Enter the Route ID : ")
				query = f"SELECT * FROM ROUTE_MANAGEMENT WHERE ROUTE_ID='{routeID}'"
				cursor.execute(query)
				print(f"{routeID} : ")
				print(cursor.fetchone())
				print("You can see more Route details!! ")
				choice = input("Want to Continue (y/n) : ")
				if choice.lower() != 'y':
					break

	#_main_Route Management
	print("Welcome to the Route Module")
	print("NOTE: If any details are unknown to you then skip it or type NULL except for the Route ID, Seats Capacity and number of trips, which are must.")
	
	while True:
		print("Select:\n1. Upload Details\n2. Update Details\n3. Delete Details\n4. View Details\n5. Exit Module")
		choice = input("Your choice : ")
		if choice == '1':
			insertRoute(cursor, database)
		elif choice == '2':
			updateRoute(cursor, database)
		elif choice == '3':
			deleteRoute(cursor, database)
		elif choice == '4':
			fetchRoute(cursor, database)
		elif choice == '5':
			print("Exited Route Module.")
			break
		else:
			print("Sorry, the operation you are in search of doesnot exist or in implementation!")
	#end of Route Management


def Employee_Management(cursor, database):
	#inserting into employee management
	def insertEmployee(cursor, database):
		print("You can now Add Data!")
		while True:
			print("Enter the details following...")
			employeeID = input("Employee ID : ")
			employeeName = input("Employee NAME : ")
			employeeAge = input("Employee AGE : ")
			shiftStartTime = input("Starting time of the shift(hh:mm:ss) : ")
			shiftEndTime = input("Ending time of the shift(hh:mm:ss) : ")
			employeeBusID = input("Employee's Bus ID : ")
			routeID = input("Route ID : ")
			overTime = int(input("Number of over time duty hours : "))
			wage = int(input("Daily wage (in Rs) : "))
			overTimeWage=int(input("Overtime duty wage per hour (in Rs) : "))
			bankAccountNumber = input("Employee's Bank Account Number : ") 
			query = f"INSERT INTO EMPLOYEE_MANAGEMENT VALUES('{employeeID}','{employeeName}','{employeeAge}','{shiftStartTime}','{shiftEndTime}','{employeeBusID}','{routeID}',{overTime},{wage},{overTimeWage},'{bankAccountNumber}')"
			cursor.execute(query)
			database.commit()
			choice = input("Do you want to insert more data(y/n) : ")
			if choice.lower() != 'y':
				break

	#updating employee management
	def updateEmployee(cursor, database):
		print("You can now Update the details!")
		print("NOTE: Enter all data including the updated ones.")
		print("Enter the following...")
		employeeID = input("Employee id : ")
		employeeIDUpdated = input("Updated Employee ID : ")
		employeeName = input("Updated Employee Name : ")
		employeeAge = input("Updated Employee Age : ")
		shiftStartTime = input("Updated starting time of the Shift(hh:mm:ss) : ")
		shiftEndTime = input("Updated ending time of the shift(hh:mm:ss) : ")
		busID = input("Updated Bus ID : ")
		routeID = input("Updated Route id : ")
		ot = int(input("Updated number of over time duty hours : "))
		wage = int(input("Updated daily wage (in Rs) : "))
		otWage = int(input("Updated Overtime duty wage per hour (in Rs) : "))
		bankAccountNumber = input("Updated Bank Account Number : ")
		query = f"UPDATE EMPLOYEE_MANAGEMENT SET EMPLOYEE_ID='{employeeIDUpdated}',EMPLOYEE_NAME='{employeeName}',AGE='{employeeAge}',SHIFT_STARTS_AT='{shiftStartTime}',SHIFT_ENDS_AT='{shiftEndTime}',BUS_ID='{busID}',ROUTE_ID='{routeID}',OT_HOURS={ot},DAILY_WAGE={wage},OT_WAGE_PER_HOUR={otWage},BANK_ACCOUNT_NUMBER='{bankAccountNumber}' WHERE EMPLOYEE_ID = '{employeeID}' " #ROUTE_ID=''"
		cursor.execute(query)
		database.commit()
		print('DONE!!')

	#deleting from employee management
	def deleteEmployee(cursor, database):
		print('You can now Delete any record!')
		employeeID = input("Enter the Employee id : ")
		query = f"DELETE FROM EMPLOYEE_MANAGEMENT WHERE EMPLOYEE_ID='{employeeID}'"
		cursor.execute(query)
		database.commit()
		print('Done!')

	#seeing details of employee management
	def fetchEmployee(cursor, database):
		print('You can now view details!')
		choice = input("View the whole Employee Data ? (y/n) : ")
		if choice.lower() == 'y':
			query = "SELECT * FROM EMPLOYEE_MANAGEMENT"
			cursor.execute(query)
			data = cursor.fetchall()
			for detail in data:
				print(detail)
		else:
			print("You can view single Employee detail at a time!")
			while True:
				employeeID = input("Enter the Employee id : ")
				query = f"SELECT * FROM EMPLOYEE_MANAGEMENT WHERE EMPLOYEE_ID='{employeeID}'"
				cursor.execute(query)
				print(cursor.fetchone())
				print('You can see more Route details!! ')

	#calculation of salary in employee management
	def salaryEmployee(cursor, database):
		print("Enter the details following...")
		employeeID = input("Employee id: ")
		days = float(input("Number of days of daily work : "))
		otDays = float(input("Number of over duty days : "))
		query = f"SELECT ((DAILY_WAGE*{days})+({otDays}*OT_HOURS*OT_WAGE_PER_HOUR)) FROM EMPLOYEE_MANAGEMENT WHERE EMPLOYEE_ID='{employeeID}'"
		cursor.execute(query)
		data = cursor.fetchone()
		for i in data : 
			print(f"Salary of Employee with ID : {employeeID} is {i}")

	#_main_employee management
	print("Welcome to the Employee module")
	print("NOTE: If any details are unknown to you then skip it or type NULL except for OT, Wage and OTwage, which are must.")
	while True:
		print("Select :\n1. Uploading data\n2. Updating data\n3. Deleting Data\n4. Accesing Data\n5. Salary Calculation\n6. Exit Module")
		choice = input("Your choice : ")
		if choice == '1' :
			insertEmployee(cursor, database)
		elif choice == '2' :
			updateEmployee(cursor, database)
		elif choice == '3' :
			deleteEmployee(cursor, database)
		elif choice == '4' :
			fetchEmployee(cursor, database)
		elif choice == '5' :
			salaryEmployee(cursor, database)
		elif choice == '6' :
			print("Exited Employee Module")
			break
		else:
			print("Sorry, the operation you are in search of doesnot exist or in implementation!")
	#end of Employee Management

#PASSENGER MODULE
def Passenger_Management(cursor, database):
	#inserting into Passenger Management
	def insertPassenger(cursor, database):
		print("You can now Add Data.")
		try:
			print("Enter the details following...")
			passengerID = input("Passenger ID : ")
			passengerName = input("Passenger Name : ")
			passengerAge = input("Passenger Age : ")
			passengerGender = input("Passenger's Gender : ")
			ticketNumber = input("Ticket Number : ")
			identityNumber = input("Government Authorized Identity Number : ")
			phoneNumber = input("Contact Number : ")
			busID = input("Boarded Bus ID : ")
			routeID = input("Boarded Bus Route id : ")
			seatNumber = input("Seat Number : ")
			boardingPlace = input("Place of Boarding : ")
			destinationPlace = input("Place of Destination : ")
			query = f"INSERT INTO PASSENGER_MANAGEMENT VALUES('{passengerID}','{passengerName}','{passengerAge}','{passengerGender}','{ticketNumber}','{identityNumber}','{phoneNumber}','{busID}','{routeID}','{seatNumber}','{boardingPlace}','{destinationPlace}')"
			cursor.execute(query)
			database.commit()
		except:    #mysql connector Integrity error
			print("The Passenger details are already available in the Database\nYou can update them!")

	#updating Passenger Management
	def updatePassenger(cursor, database):
		print("You can now Update the Passenger details")
		print("Note: Government Authorized Identity number cannot be updated!")
		print("Enter the details following...")
		passengerID = input("ID of passenger to be updated : ")
		passengerName = input("Updated Passenger Name : ")
		passengerAge = input("Updated Passenger Age : ")
		passengerGender = input("Updated Passenger Gender : ")
		ticketNumber = input("Updated Ticket Number : ")
		phoneNumber = input("Updated Contact Number : ")
		busID = input("Updated Bus ID : ")
		routeID = input("Updated Route id : ")
		seatNumber = input("Updated Seat number : ")
		boardingPlace = input("Updated Place of Boarding : ")
		destinationPlace = input("Updated Place of Destination : ")
		query = f"UPDATE PASSENGER_MANAGEMENT SET PASSENGER_NAME='{passengerName}',AGE='{passengerAge}',GENDER='{passengerGender}',TICKET_NO='{ticketNumber}',PHONE_NO='{phoneNumber}',BUS_ID='{busID}',ROUTE_ID='{routeID}',SEAT_NO='{seatNumber}',PLACE_OF_BOARDING='{boardingPlace}',PLACE_OF_DESTINATION='{destinationPlace}' WHERE PASSENGER_ID='{passengerID}'"
		cursor.execute(query)
		database.commit()

	#deleting from Passenger Management
	def deletePassenger(cursor, database):
		print("You can now Delete any record!")
		try:
			choice = input("Want to delete through Passenger ID or GAI Number (I/G) : ")
			if choice.lower() == 'i':
				passengerID = input("Enter the Passenger ID to delete the details : ")
				query = f"DELETE FROM PASSENGER_MANAGEMENT WHERE PASSENGER_ID='{passengerID}'"
				cursor.execute(query)
				database.commit()
				print('Done!')
			elif choice.lower() == 'G':
				GAI = input("Enter the Government Authorized Identity Number of Passenger to delete the details : ")
				query = f"DELETE FROM PASSENGER_MANAGEMENT WHERE AADHAR_NO='{GAI}'"
				cursor.execute(query)
				database.commit()
				print('Done!')
		except:
			print("Invalid! You have chosen neither options provided.")
			

	#seeing details of Passenger Management
	def fetchPassenger(cursor, database):
		print("You can now view details!")
		choice = input("Want to view the whole passenger daetails (y/n) : ")
		if choice.lower() == 'y':
			query = "SELECT * FROM PASSENGER_MANAGEMENT"
			cursor.execute(query)
			details = cursor.fetchall()
			print("All the Passenger Details:")
			for detail in details:
				print(detail)
		else:
			print("You can view a single passenger detail at a time!")
			while True:
				passngerID = input("Enter the Passenger ID : ")
				query = f"SELECT * FROM PASSENGER_MANAGEMENT WHERE PASSENGER_ID='{passngerID}'"
				cursor.execute(query)
				print(cursor.fetchone())
				print("You can view more Passenger details!!")
				choice = input("Want to Continue (y/n) : ")
				if choice.lower() != 'y':
					break

	#_main_Passenger Management
	print("Welcome to the Passenger Module")
	print("NOTE: If any details are unknown to you then skip it or type NULL except for Passenger ID and Government Authorized ID Number")
	
	while True:
		print("Select:\n1. Upload Details\n2. Update Details\n3. Delete records\n4. View Details\n5. Exit")
		choice = input("Your choice : ")
		if choice == '1':
			insertPassenger(cursor, database)
		elif choice == '2':
			updatePassenger(cursor, database)
		elif choice == '3':
			deletePassenger(cursor, database)
		elif choice == '4':
			fetchPassenger(cursor, database)
		elif choice == '5':
			print("Exited Passenger Module")
			break
		else:
			print("Sorry, the operation you are in search of doesnot exist or in implementation!")
	#end of Passenger Management

#_MAIN_PROGRAM		
if __name__ == "__main__" :
	print('Welcome to''\n''The ELITE BUS TRAVELS')
	hostName = input("Enter the Host name (generally 'localhost') : ")
	userName = input("Enter the Username (generally 'root') : ")
	databaseName = input("Enter the Database name : ")
	password = input("Enter the password : ")

	database = sql.connect(host = hostName, user = userName, password = password, database = databaseName)
	if database.is_connected():
			print("Successfully connected...Your Database is Ready to Start!")
	else:
			print("The Database you need doesnot exist!")
	cursor = database.cursor()
	try:
		while True:
			print("Select :\n1. Bus Management\n2. Employee Management\n3. Route Management\n4. Passenger Management\n5. Exit the Application")
			moduleChoice = input("Enter the associated number of your selected module : ")
			if moduleChoice == '1':
				Bus_Management(cursor, database)
			elif moduleChoice == '2':
				Employee_Management(cursor, database)
			elif moduleChoice == '3':
				Route_Management(cursor, database)
			elif moduleChoice == '4':
				Passenger_Management(cursor, database)
			elif moduleChoice == '5':
				break
			else:
				print("Sorry, the module you are in search of doesnot exist or in implementation!")
	except:
		print("Sorry! There's some error encountered. Exiting...")
	database.close()
	print('Thank You for Visiting!')
