#VEHICLE MANAGEMENT SYSTEM
def Bus_Management():
	#Inserting into Bus Management
	def insertbm():
		while True:
			id1=input('Enter the BUSID:')
			type=input('Enter AC or NON-AC:')
			company=input('Enter the Bus Company:')
			no1=input('Enter the Registered Vehicle Number:')
			fuel=input('Enter the Fuel used:')
			cap1=input('Enter the Seats Capacity:')
			mileage=input('Enter the mileage of vehicle per litre:')
			ser1=input('Enter the date of last service done(YYYY-MM-DD):')
			str1="INSERT INTO BUS_MANAGEMENT VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(id1,type,company,no1,fuel,cap1,mileage,ser1)
			cur1.execute(str1)
			db.commit()
			ch3=input('Do you want to insert more data(y/n):')
			if ch3.lower()=='n':
				break	

	#updating Bus Management
	def updatebm():
		while True:
			bmupdate=input('Enter the BusId you want to update:')
			type=input('Enter AC or NON-AC:')
			company=input('Enter the Bus Company:')
			no1=input('Enter the Registered Vehicle Number:')
			fuel=input('Enter the Fuel used:')
			cap1=input('Enter the Seats Capacity:')
			mileage=input('Enter the mileage of vehicle per litre:')
			ser1=input('Enter the date of last service done(YYYY-MM-DD):')
			str2="UPDATE BUS_MANAGEMENT SET TYPE='{}',COMPANY='{}',REGISTERED_NO='{}',FUEL='{}',SEATS_CAPACITY='{}',MILEAGE='{}',LAST_SERVICE_DONE='{}' WHERE BUS_ID='{}'".format(type,company,no1,fuel,cap1,mileage,ser1,bmupdate)
			cur1.execute(str2)
			db.commit()
			print('DONE!!')
			ch3=input('Continue with Updating other records(y/n):')
			if ch3.lower()=='n':
				break

	#deleting in bus management
	def deletebm():
			while True:
				name3=input('Enter the Bus id to delete its details:')
				str6="DELETE FROM BUS_MANAGEMENT WHERE BUS_ID='{}'".format(name3)
				cur1.execute(str6)
				db.commit()
				ch4=input('Continue in Deleting other records(y/n):')
				if ch4.lower()=='n':
					break

	#showing details of Bus Management
	def fetchbm():
		print('You can now see bus details!')
		ch=input('Want to see the whole data(y/n):')
		if ch.lower()=='y':
			str9='SELECT * FROM BUS_MANAGEMENT'
			cur1.execute(str9)
			data5=cur1.fetchall()
			for i in data5:
				print(i)
		else:
			print('Can see single record at a time!')
			while True:
				id6=input('Enter the Bus code:')
				str9="SELECT * FROM BUS_MANAGEMENT WHERE BUS_ID='{}'".format(id6)
				cur1.execute(str9)
				print(cur1.fetchone())
				print('You can see more Route details!! ')
				ch7=input('Want to Continue(y/n):')
				if ch7.lower()=='n':
					break

	#_main_Bus Management
	print('Welcome to the Bus Management module:')
	print('NOTE: If any details are unknown to you then skip it or type NULL')
	name=input('Enter the name of the database:')
	import mysql.connector as c
	db=c.connect(host='localhost',user='sai',password='',database=name)
	if db.is_connected():
			print('Your Database is Ready to Start.')
	else:
			print('The Database you need doesnot exist ')
	cur1=db.cursor()
	while True:
		print("i for uploading data")
		print('u for updating')
		print('d for deleting data')
		print('f for accesing data')
		ch2=input('Enter the function you need:')
		if ch2.lower()=='i':
			insertbm()
		elif ch2.lower()=='u':
			updatebm()
		elif ch2.lower()=='d':
			deletebm()
		elif ch2.lower()=='f':
			fetchbm()
		else:
			print('The Function you are in search of doesnot exist or in implementation!')
		choose=input('continue with BUS MANAGEMENT(y/n):')
		if choose.lower()=='n':
			break
	db.close()
	#end of Bus Management

	
def Route_Management():
	#inserting into ROUTE MANAGEMENT
	def insertrm():
		print('You can now Add Data!')
		while True:
			id2=input('Enter the ROUTEID:')
			fro=input('Enter the FROM place:')
			to1=input('Enter the TO place:')
			cib1=input('Enter the Cities in between the route:')
			bid=input('Enter the Dedicated Bus Id for the route:')
			estd=input('Enter the estimated duration of journey:')
			cap2=input('Enter the Seats Available:')
			trips=input('Enter the no. of trips per day:')
			str3="INSERT INTO ROUTE_MANAGEMENT VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(id2,fro,to1,cib1,bid,estd,trips,cap2)
			cur2.execute(str3)
			db.commit()
			ch4=input('Do you want to insert more data(y/n):')
			if ch4.lower()=='n':
				break		

	#Updating Route Management
	def updaterm():
		print('You can now Update!')
		while True:
			rmupdate=input('Enter the BusId you want to update:')
			fro=input('Enter updated FROM place:')
			to2=input('Enter updated TO place:')
			cib2=input('Enter updated cities in between:')
			bid=input('Enter updated Dedicated Bus Id for the route:')
			estd=input('Enter updated estimated duration of journey:')
			cap2=input('Enter updated Seats Available:')
			trips=input('Enter updated no. of trips per days:')
			str4="UPDATE ROUTE_MANAGEMENT SET FROM_PLACE='{}',TO_PLACE='{}',CITIES_IN_BETWEEN='{}',DEDICATED_BUSID='{}',DURATION='{}',TRIPS_PER_DAY='{}',AVAILABLE_SEATS='{}' WHERE ROUTE_ID='{}'".format(fro,to2,cib2,bid,estd,trips,cap2,rmupdate)
			cur2.execute(str4)
			db.commit()
			print('DONE!!')
			ch5=input('Continue with Updating other records(y/n):')
			if ch5.lower()=='n':
				break	

	#Delete from Route Management
	def deleterm():
		print('You can now Delete any record!')
		while True:
				name4=input('Enter the Route id to delete its details:')
				str5="DELETE FROM ROUTE_MANAGEMENT WHERE ROUTE_ID='{}'".format(name4)
				cur2.execute(str5)
				db.commit()
				print('Done!')
				ch4=input('Continue in Deleting other records(y/n):')
				if ch4.lower()=='n':
					break
	
	#seeing deatils of Route Management
	def fetchrm():
		print('You can now see details!')
		ch=input('Want to see the whole data(y/n):')
		if ch.lower()=='y':
			str7='SELECT * FROM ROUTE_MANAGEMENT'
			cur2.execute(str7)
			data4=cur2.fetchall()
			for i in data4:
				print(i)
		else:
			print('Can see single record at a time!')
			while True:
				id6=input('Enter the Route code:')
				str8="SELECT * FROM ROUTE_MANAGEMENT WHERE ROUTE_ID='{}'".format(id6)
				cur2.execute(str8)
				print(cur2.fetchone())
				print('You can see more Route details!! ')
				ch7=input('Want to Continue(y/n):')
				if ch7.lower()=='n':
					break

	#_main_Route Management
	print('Welcome to the Route Management module')
	print('NOTE: If any details are unknown to you then skip it or type NULL')
	name2=input('Enter the name of the database:')
	import mysql.connector as c
	db=c.connect(host='localhost',user='sai',password='',database=name2)
	if db.is_connected():
			print('Your Database is Ready to Start.')
	else:
			print('The Database you need doesnot exist ')
	cur2=db.cursor()
	while True:
		print("i for uploading data")
		print('u for updating')
		print('d for deleting data')
		print('f for accesing data')
		ch5=input('Enter the function you need:')
		if ch5.lower()=='i':
			insertrm()
		elif ch5.lower()=='u':
			updaterm()
		elif ch5.lower()=='d':
			deleterm()
		elif ch5.lower()=='f':
			fetchrm()
		else:
			print('The Function you are in search of doesnot exist or in implementation!')
		choose1=input('continue with ROUTE MANAGEMENT(y/n):')
		if choose1.lower()=='n':
			break
	db.close()
	#end of Route Management


def Employee_Management():
	#inserting into employee management
	def insertem():
		print('You can now Add Data!')
		while True:
			id3=input('Enter the EMPLOYEE ID:')
			name=input('Enter the EMPLOYEE NAME:')
			age=input('Enter the EMPLOYEE AGE:')
			shift_start=input('Enter the starting time of the Shift(hh:mm:ss) :')
			shift_end=input('Enter the ending time of the shift(hh:mm:ss):')
			busid=input('Enter the Bus id :')
			routeid =input('Enter the Route id:')
			ot=int(input('Enter the number of over time duty hours :'))
			wage=int(input('Enter the daily wage (in Rs):'))
			otwage=int(input('Enter the Overtime dvuty wage per hour (in Rs) :'))
			bank=input('Enter the Bank Account Number:') 
			str3="INSERT INTO EMPLOYEE_MANAGEMENT VALUES('{}','{}','{}','{}','{}','{}','{}',{},{},{},'{}')".format('id3','name','age','shift_start','shift_end','busid','routeid',ot,wage,otwage,'bank')
			cur3.execute(str3)
			db.commit()
			ch4=input('Do you want to insert more data(y/n):')
			if ch4.lower()=='n':
				break

	#updating employee management
	def updateem():
		print('You can now Update!')
		print('NOTE: Enter all data including the updated data.')
		while True:
			emupdate=input('Enter the Employee id to be updated:')
			id3=input('Enter updated EMPLOYEEID:')
			name=input('Enter updated EMPLOYEE NAME:')
			age=input('Enter updated EMPLOYEE AGE:')
			shift_start=input('Enter updated starting time of updated Shift(hh:mm:ss) :')
			shift_end=input('Enter updated ending time of the shift(hh:mm:ss):')
			busid=input('Enter updated Bus id :')
			routeid =input('Enter updated Route id:')
			ot=int(input('Enter updated number of over time duty hours :'))
			wage=int(input('Enter updated daily wage (in Rs):'))
			otwage=int(input('Enter updated Overtime duty wage per hour (in Rs) :'))
			bank=input('Enter updated Bank Account Number:') 
			str4="UPDATE EMPLOYEE_MANAGEMENT SET EMPLOYEE_ID='id3',EMPLOYEE_NAME='name',AGE='age',SHIFT_STARTS_AT='shift_start',SHIFT_ENDS_AT='shift_end',BUS_ID='busid',ROUTE_ID='routeid',OT_HOURS=ot,DAILY_WAGE=wage,OT_WAGE_PER_HOUR=otwage,BANK_ACCOUNT_NUMBER='bank' WHERE ROUTE_ID='emupdate'"
			cur3.execute(str4)
			db.commit()
			print('DONE!!')
			ch5=input('Continue with Updating other records(y/n):')
			if ch5.lower()=='n':
				break

	#deleting from employee management
	def deleteem():
		print('You can now Delete any record!')
		while True:
				name4=input('Enter the Employee id to delete his/her details:')
				str5="DELETE FROM EMPLOYEE_MANAGEMENT WHERE EMPLOYEE_ID='{}'".format('name4')
				cur3.execute(str5)
				db.commit()
				print('Done!')
				ch4=input('Continue in Deleting other records(y/n):')
				if ch4.lower()=='n':
					break

	#seeing details of employee management
	def fetchem():
		print('You can now see details!')
		ch=input('Want to see the whole Employee Data(y/n):')
		if ch.lower()=='y':
			str7='SELECT * FROM EMPLOYEE_MANAGEMENT'
			cur3.execute(str7)
			data4=cur3.fetchall()
			for i in data4:
				print(i)
		else:
			print('Can see single Employee detail at a time!')
			while True:
				id6=input('Enter the Employee id:')
				str8="SELECT * FROM EMPLOYEE_MANAGEMENT WHERE EMPLOYEE_ID='{}'".format('id6')
				cur3.execute(str8)
				print(cur3.fetchone())
				print('You can see more Route details!! ')
				ch7=input('Want to Continue(y/n):')
				if ch7.lower()=='n':
					break

	#calculation of salary in employee management
	def salaryem():
		id9=input('Enter the Employee id:')
		days=float(input('Enter the number of days of daily working:'))
		otdays=float(input('Enter the number of over duty days:'))
		str8="SELECT ((DAILY_WAGE*{})+({}*OT_HOURS*OT_WAGE_PER_HOUR)) FROM EMPLOYEE_MANAGEMENT WHERE EMPLOYEE_ID='{}'".format(days,otdays,id9)
		cur3.execute(str8)
		data6=cur3.fetchone()
		for i in data6: 
			print('SALARY IS',i)

	#_main_employee management
	print('Welcome to the Employee Management module')
	print('NOTE: If any details are unknown to you then skip it or type NULL')
	name2=input('Enter the name of the database:')
	import mysql.connector as c
	db=c.connect(host='localhost',user='sai',password='',database=name2)
	if db.is_connected():
			print('Your Database is Ready to Start.')
	else:
			print('The Database you need doesnot exist ')
	cur3=db.cursor()
	while True:
		print("i for uploading data")
		print('u for updating')
		print('d for deleting data')
		print('f for accesing data')
		print('s for salary calculation')
		ch5=input('Enter the function you need:')
		if ch5.lower()=='i':
			insertem()
		elif ch5.lower()=='u':
			updateem()
		elif ch5.lower()=='d':
			deleteem()
		elif ch5.lower()=='f':
			fetchem()
		elif ch5.lower()=='s':
			salaryem()
		else:
			print('The Function you are in search of doesnot exist or in implementation!')
		choose1=input('continue with EMPLOYEE  MANAGEMENT(y/n):')
		if choose1.lower()=='n':
			break
	db.close()
	#end of Employee Management


def Passenger_Management():
	#inserting into Passenger Management
	def insertpm():
		print('You can now Add Data!')
		while True:
			try:
				id4=input('Enter the PASSENGER_ID:')
				name=input('Enter the Passenger Name:')
				age=input('Enter the Passenger Age:')
				gender=input('Enter the Gender:')
				tno=input('Enter the Ticket Number:')
				ano=input('Enter the Adhaar Number:')
				pno=input('Enter the Contact Number:')
				busid=input('Enter the Bus id:')
				routeid=input('Enter the Route id:')
				sno=input('Enter the Seat number:')
				fplace=input('Enter the Boarding place:')
				tplace=input('Enter the Destination:')
				str7="INSERT INTO PASSENGER_MANAGEMENT VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id4,name,age,gender,tno,ano,pno,busid,routeid,sno,fplace,tplace)
				cur4.execute(str7)
				db.commit()
			except:    #mysql connector Integrity error
				print('The Passenger details are already available in the Database')
			ch4=input('Do you want to insert more data(y/n):')
			if ch4.lower()=='n':
				break

	#updating Passenger Management
	def updatepm():
		print('You can now Update')
		print('Note: Adhaar number cannot be updated')
		while True:
				id4=input('Enter the PASSENGER_ID to be updated:')
				name=input('Enter updated Passenger Name:')
				age=input('Enter updated Passenger Age:')
				gender=input('Enter updated Gender:')
				tno=input('Enter updated Ticket Number:')
				pno=input('Enter updated Contact Number:')
				busid=input('Enter updated Bus id:')
				routeid=input('Enter updated Route id:')
				sno=input('Enter updated Seat number:')
				fplace=input('Enter updated Boarding place:')
				tplace=input('Enter updated Destination:')
				str7="UPDATE PASSENGER_MANAGEMENT SET PASSENGER_NAME='{}',AGE='{}',GENDER='{}',TICKET_NO='{}',PHONE_NO='{}',BUS_ID='{}',ROUTE_ID='{}',SEAT_NO='{}',FROM_PLACE='{}',TO_PLACE='{}' WHERE PASSENGER_ID='{}'".format(name,age,gender,tno,pno,busid,routeid,sno,fplace,tplace,id4)
				cur4.execute(str7)
				db.commit()
				ch4=input('Do you want to insert more data(y/n):')
				if ch4.lower()=='n':
					break

	#deleting from Passenger Management
	def deletepm():
		print('You can now Delete any record!')
		while True:
			try:
				ch=input('Want to delete through id or adhaar number(i/a):')
				if ch.lower()=='i':
					name4=input('Enter the Passenger id to delete his/her details:')
					str5="DELETE FROM PASSENGER_MANAGEMENT WHERE PASSENGER_ID='{}'".format(name4)
					cur4.execute(str5)
					db.commit()
					print('Done!')
				elif ch.lower()=='a':
					name5=input('Enter the adhaar number of  Passenger to delete his/her details:')
					str6="DELETE FROM PASSENGER_MANAGEMENT WHERE AADHAR_NO='{}'".format(name5)
					cur4.execute(str6)
					db.commit()
					print('Done!')
			except:
				print('You have chosen another way which is not available.')
			ch4=input('Continue in Deleting other records(y/n):')
			if ch4.lower()=='n':
					break

	#seeing details of Passenger Management
	def fetchpm():
		print('You can now see details!')
		ch=input('Want to see the whole data(y/n):')
		if ch.lower()=='y':
			str7='SELECT * FROM PASSENGER_MANAGEMENT'
			cur4.execute(str7)
			data4=cur4.fetchall()
			for i in data4:
				print(i)
		else:
			print('Can see single passenger detail at a time!')
			while True:
				id6=input('Enter the Passenger id:')
				str8="SELECT * FROM PASSENGER_MANAGEMENT WHERE PASSENGER_ID='{}'".format(id6)
				cur4.execute(str8)
				print(cur4.fetchone())
				print('You can see more Passenger details!! ')
				ch7=input('Want to Continue(y/n):')
				if ch7.lower()=='n':
					break

	#_main_Passenger Management
	print('Welcome to the Passenger Management module')
	print('NOTE: If any details are unknown to you then skip it or type NULL')
	name2=input('Enter the name of the database:')
	import mysql.connector as c
	db=c.connect(host='localhost',user='sai',password='',database=name2)
	if db.is_connected():
			print('Your Database is Ready to Start.')
	else:
			print('The Database you need doesnot exist ')
	cur4=db.cursor()
	while True:
		print("i for uploading data")
		print('u for updating')
		print('d for deleting data')
		print('f for accesing data')
		ch5=input('Enter the function you need:')
		if ch5.lower()=='i':
			insertpm()
		elif ch5.lower()=='u':
			updatepm()
		elif ch5.lower()=='d':
			deletepm()
		elif ch5.lower()=='f':
			fetchpm()
		else:
			print('The Function you are in search of doesnot exist or in implementation!')
		choose1=input('continue with PASSENGER  MANAGEMENT(y/n):')
		if choose1.lower()=='n':
			break
	db.close()
	#end of Passenger Management

#_MAIN_PROGRAM
def home():
	print('Enter 1 for Bus Management')
	print('Enter 2 for Employee Management')
	print('Enter 3 for Route Management')
	print('Enter 4 for Passenger Management')
	com=int(input('Enter the associated number of your selected module:'))
	if com==int(1):
		Bus_Management()
	elif com==int(2):
		Employee_Management()
	elif com==int(3):
		Route_Management()
	elif com==int(4):
		Passenger_Management()
	else:
		print('The Function you are in search of doesnot exist or in implementation!')
print('WELCOME TO''\n''The ELITE BUS TRAVELS')
		
home()    #PROGRAM STARTS HERE!!!

while True:     #reiterating and using functions
	ch=input('Do you want to continue with other managements? (y/n):')
	if ch.lower()=='y':
		home()
	else:
		break
print('Thank You for Visiting!')
#PROGRAM ENDS HERE!!!
