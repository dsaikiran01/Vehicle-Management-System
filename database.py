import mysql.connector as sql

def table_creation():
	hostName = input("Enter the Host Name (generally localhost) : ")
	userName = input("Enter the User Name (generally root) : ")
	databaseName = input('Enter the Name of the database :')
	password = input("Enter the password : ")
	database = sql.connect(host = hostName, user = userName, password = password, database = databaseName)	#database connection
	cursor = database.cursor()   #cursor object
	busManagementTable = "CREATE TABLE IF NOT EXISTS BUS_MANAGEMENT(BUS_ID VARCHAR(100) PRIMARY KEY,TYPE VARCHAR(20),MANUFACTURER VARCHAR(30),REGISTERED_NO VARCHAR(30),FUEL FLOAT(6),SEATS_CAPACITY INT(2),MILEAGE FLOAT(6),LAST_SERVICE_DONE DATE)"	###bus management table###
	cursor.execute(busManagementTable)
	database.commit()
	routeManagementtable = "CREATE TABLE IF NOT EXISTS ROUTE_MANAGEMENT(ROUTE_ID VARCHAR(100) PRIMARY KEY,PLACE_OF_BOARDING VARCHAR(30),PLACE_OF_DESTINATION VARCHAR(30),CITIES_IN_BETWEEN VARCHAR(300),DEDICATED_BUSID VARCHAR(30),DURATION VARCHAR(10),TRIPS_PER_DAY INT(2),AVAILABLE_SEATS INT(2))"	###route management table###
	cursor.execute(routeManagementtable)
	database.commit()
	employeeManagementTable = "CREATE TABLE IF NOT EXISTS EMPLOYEE_MANAGEMENT(EMPLOYEE_ID VARCHAR(100) PRIMARY KEY,EMPLOYEE_NAME VARCHAR(100),AGE VARCHAR(3),SHIFT_STARTS_AT TIME,SHIFT_ENDS_AT TIME,BUS_ID VARCHAR(100),ROUTE_ID VARCHAR(100),OT_HOURS INT(2),DAILY_WAGE INT(10),OT_WAGE_PER_HOUR INT(10),BANK_ACCOUNT_NUMBER VARCHAR(100))"	###employee management table###
	cursor.execute(employeeManagementTable)
	database.commit()
	passengerManagementTable = "CREATE TABLE IF NOT EXISTS PASSENGER_MANAGEMENT(PASSENGER_ID VARCHAR(100) PRIMARY KEY ,PASSENGER_NAME VARCHAR(100),AGE VARCHAR(3),GENDER VARCHAR(10),TICKET_NO VARCHAR(30),GOVERNMENT_AUTHORIZED_IDENTITY_NUMBER VARCHAR(15) UNIQUE,PHONE_NO VARCHAR(20),BUS_ID VARCHAR(100),ROUTE_ID VARCHAR(100),SEAT_NO VARCHAR(10),PLACE_OF_BOARDING VARCHAR(20),PLACE_OF_DESTINATION VARCHAR(30))"	###passenger management table### 
	cursor.execute(passengerManagementTable)
	database.commit()
	print(f"Succesfully created the tables in {databaseName} !!!")

#main
if __name__ == "__main__" :
	try:
		table_creation() 
	except:
		print("Error while creating connection with the database and creating tables...\nExiting...")
