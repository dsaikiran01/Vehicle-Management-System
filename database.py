def table_creation():
	name1=input('Enter the Name of the database:')
	import mysql.connector as s
	db=s.connect(host='localhost',user='root',password='',database=name1)	#database connection
	c=db.cursor()   #cursor object
	table1="CREATE TABLE BUS_MANAGEMENT(BUS_ID VARCHAR(100) PRIMARY KEY,TYPE VARCHAR(20),COMPANY VARCHAR(30),REGISTERED_NO VARCHAR(30),FUEL VARCHAR(20),SEATS_CAPACITY VARCHAR(3),MILEAGE VARCHAR(3),LAST_SERVICE_DONE DATE)"	###bus management table###
	c.execute(table1)
	db.commit()
	table2="CREATE TABLE ROUTE_MANAGEMENT(ROUTE_ID VARCHAR(100) PRIMARY KEY,FROM_PLACE VARCHAR(30),TO_PLACE VARCHAR(30),CITIES_IN_BETWEEN VARCHAR(300),DEDICATED_BUSID VARCHAR(30),DURATION VARCHAR(10),TRIPS_PER_DAY VARCHAR(3),AVAILABLE_SEATS VARCHAR(2))"	###route management table###
	c.execute(table2)
	db.commit()
	table3="CREATE TABLE EMPLOYEE_MANAGEMENT(EMPLOYEE_ID VARCHAR(100) PRIMARY KEY,EMPLOYEE_NAME VARCHAR(100),AGE VARCHAR(3),SHIFT_STARTS_AT TIME,SHIFT_ENDS_AT TIME,BUS_ID VARCHAR(100),ROUTE_ID VARCHAR(100),OT_HOURS INT(2),DAILY_WAGE INT(10),OT_WAGE_PER_HOUR INT(10),BANK_ACCOUNT_NUMBER VARCHAR(100))"	###employee management table###
	c.execute(table3)
	db.commit()
	table4="CREATE TABLE PASSENGER_MANAGEMENT(PASSENGER_ID VARCHAR(100) PRIMARY KEY ,PASSENGER_NAME VARCHAR(100),AGE VARCHAR(3),GENDER VARCHAR(10),TICKET_NO VARCHAR(30),ADHAAR_NO VARCHAR(15) UNIQUE,PHONE_NO VARCHAR(20),BUS_ID VARCHAR(100),ROUTE_ID VARCHAR(100),SEAT_NO VARCHAR(10),FROM_PLACE VARCHAR(20),TO_PLACE VARCHAR(30))"	###passenger management table### 
	c.execute(table4)
	db.commit()
	print('SUCCESSFUL')
	print('TABLES CREATED IN',name1)

#main
if __name__ == '__main__' :
	try:
		table_creation()   #starting 
	except:
		print("Error while creating database...\nExiting...")
#THE END
