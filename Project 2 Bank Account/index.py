import getpass as gp
import sqlite3 as sql
import prettytable as PT
import datetime as DT
import time 
import random as rnd
import re
from os import system
from time import sleep

global AdId
global AcId

BankCon=sql.connect("bank.db")
BankCus=BankCon.cursor()
q='''
CREATE TABLE if not exists Admin(
	admId integer PRIMARY KEY AUTOINCREMENT,
	AName TEXT NOT NULL,
	APass TEXT  UNIQUE NOT NULL
)
'''
BankCus.execute(q)# owner of the bank

q='''
CREATE TABLE if not exists Acct(
	AcctId integer PRIMARY KEY AUTOINCREMENT,
	AcctName TEXT NOT NULL,
	AcctPass TEXT UNIQUE NOT NULL
)
'''
BankCus.execute(q)#for the accountant

q='''
CREATE TABLE IF not exists User(
	UserId integer PRIMARY KEY AUTOINCREMENT,
	AId integer not null,
	U_Name  text not null,
	U_Gender text not null,
	U_Age integer not null check (U_Age>=18),
	U_FName text not null,
	U_DOB date not null,
	U_Mobile integer not null,
	U_AccNum TEXT NOT NULL,
	U_Balance integer not null check (U_Balance>=5000),
	FOREIGN KEY (AId) REFERENCES Acct(AcctId)
)
'''
BankCus.execute(q)#bank customer who has his account in the bank

q='''
CREATE TABLE if not exists trans(
	TransId integer primary key AUTOINCREMENT,
	UId integer not null,
	AId integer not null,
	initial int not null,
	Amt int not null,
	flag TEXT not null,
	Balance integer not null,
	TransDate date not null,
	TransTime text not null,
	FOREIGN KEY (UId) REFERENCES User(UserId),
	FOREIGN KEY (Balance) REFERENCES User(U_Balance),
	FOREIGN KEY (AId) REFERENCES Acct(AcctId)
)
'''
BankCus.execute(q)#record of transactions done by accountant flag CR(Credit) DB(Debit)

q='''
CREATE TABLE if not exists Logs(
	logId integer PRIMARY KEY AUTOINCREMENT,
	tId integer,
	aId integer,
	uId integer,
	flag text not null,
	lDate date NOT NULL, 
	lTime text not null,
	FOREIGN KEY (tId) REFERENCES trans(TransId),
	FOREIGN KEY (aId) REFERENCES Acct(AcctId),
	FOREIGN KEY (uId) REFERENCES User(UserId)
	FOREIGN KEY (lDate) REFERENCES trans(TransDate),
	FOREIGN KEY (lTime) REFERENCES trans(TransTime)
)
'''
BankCus.execute(q)#History of all actions of bank flag= CR(credit) DB(debit) Na(New Account) Tr(Account Terminated) RM(REMOVED)

def NameCheck(name):
	if len(name)<3:
		return 0
	regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',re.IGNORECASE)
	res = regex_name.search(name)
	if res:
		return 1
	else: 
		return 0

def admin():#menu for admin
	system('cls')
	print('''
					WELCOME TO ICICI BANK
		 1) VIEW ALL ACCOUNTANTS
		 2) REMOVE ACCOUNTANT
		 3) VIEW ALL CUSTOMERS
		 4) CUSTOMER DETAILS
		 5) REMOVE CUSTOMER
		 6) CREATE NEW ADMINISTRATOR
		 7) REMOVE ADMINISTRATOR
		 8) CHANGE PASSWORD
		 9) VIEW LOGS
		10) VIEW TRANSACTIONS
		11) LOGOUT

		''')
	ch=input("ENTER YOUR CHOICE: ")
	if ch=='1':
		system('cls')
		q='''SELECT * FROM Acct'''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		if data==None:
			print("HIRE SOME ACCOUNTANTS BEFORE YOU VIEW THEM !!!")
			sleep(2)
			system('cls')
			admin()
		x=PT.PrettyTable(["ACCOUNTANT ID","ACCOUNTANT NAME","ACCOUNTANT PASSWORD"])
		for i in data:
			x.add_row(list(i))
		print(x)
		gp.getpass("PRESS ENTER TO CONTINUE")
		system('cls')
		admin()
	elif ch=='2':
		#while True: 
		val=int(input("Enter the accountant ID: "))
		q='''SELECT AcctId FROM Acct'''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		x=[]
		for i in range(len(data)):
			x.append(data[i][0])
		if val in x:
			system('cls')
			l=[val]
			q='''DELETE FROM Acct WHERE AcctId=?'''
			BankCus.execute(q,tuple(l))
			BankCon.commit()
			l=[val,"RM"]
			today = DT.date.today()
			s=str(today)
			l.append(s)
			t = time.localtime()
			current_time = time.strftime("%H:%M:%S", t)
			l.append(current_time)
			q='''INSERT INTO Logs (aId,flag,lDate,lTime) VALUES (?,?,?,?)'''
			BankCus.execute(q,tuple(l))
			BankCon.commit()
			print("RECORD DELETED SUCCESSFULLY!")
			ch=gp.getpass("Press ENTER to CONTINUE")
			system('cls')
			admin()
		else:
			print("Enter a valid accountant ID!!!")
			sleep(2)
			system('cls')
			admin()
	elif ch=='3':
		system('cls')
		q='''SELECT UserId,AId,U_AccNum,U_Balance,U_Name,U_Gender,U_FName,U_DOB,U_Age,U_Mobile FROM User'''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		if len(data)==0:
			print("GET SOME CUSTOMERS TO SEE THEIR DETAILS !!!")
			sleep(2)
			system('cls')
			admin()
		x=PT.PrettyTable(["USER ID","ACCOUNTANT ID","ACC.NUM.","BALANCE","NAME","SEX","FATHER NAME","DOB","AGE","CONTACT NO."])
		for i in data:
			x.add_row(list(i))
		print(x)
		gp.getpass("PRESS ENTER TO CONTINUE")
		system('cls')
		admin()
	elif ch=='4':
		print()
		Anum=input("ENTER THE ACCOUNT NUMBER: ")
		system('cls')
		q='''SELECT U_AccNum,U_Balance,U_Name,U_Gender,U_FName,U_DOB,U_Age,U_Mobile FROM User WHERE U_AccNum like ?'''
		heap=BankCus.execute(q,[Anum])
		data=heap.fetchone()
		if data==None:
			print("ENTER CORRECT ACCOUNT NUMBER !!!")
			gp.getpass("PRESS ENTER TO CONTINUE")
			system('cls')
			admin()
		else:
			print("\t\t\tACCOUNT DETAILS\n")
			print("ACCOUNT NUMBER: ",data[0])
			print("       BALANCE: ",data[1])
			print("          NAME: ",data[2])
			print("        GENDER: ",data[3])
			print("   FATHER NAME: ",data[4])
			print(" DATE OF BIRTH: ",data[5])
			print("           AGE: ",data[6])
			print(" MOBILE NUMBER: ",data[7])
			gp.getpass("\n\n\nPRESS ENTER TO CONTINUE")
		system('cls')
		admin()
	elif ch=='5':
		val=int(input("Enter the customer ID: "))
		q='''SELECT UserId FROM User'''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		x=[]
		for i in range(len(data)):
			x.append(data[i][0])
		if val in x:
			system('cls')
			l=[val]
			q='''DELETE FROM User WHERE UserId=?'''
			BankCus.execute(q,tuple(l))
			BankCon.commit()
			l=[val,"RM"]
			today = DT.date.today()
			s=str(today)
			l.append(s)
			t = time.localtime()
			current_time = time.strftime("%H:%M:%S", t)
			l.append(current_time)
			q='''INSERT INTO Logs (uId,flag,lDate,lTime) VALUES (?,?,?,?)'''
			BankCus.execute(q,tuple(l))
			BankCon.commit()
			print("RECORD DELETED SUCCESSFULLY!")
			ch=gp.getpass("Press ENTER to CONTINUE")
			system('cls')
			admin()
		else:
			print("Enter a valid accountant ID!!!")
			sleep(2)
			system('cls')
			admin()
	elif ch=='6':
		print()
		l=[]
		while True:
			val=input("ENTER NAME: ")
			flag=NameCheck(val)
			if flag==1:
				break
			else:
				print("Enter a valid name!!!")			
		l.append(val)
		pas=gp.getpass("ENTER PASSWORD: ")
		l.append(pas)
		try:
			q='''INSERT INTO Admin(AName,APass) VALUES(?,?)'''
			BankCus.execute(q,tuple(l))
			BankCon.commit()
			print("NEW ADMINISTRATOR CREATED")
			sleep(2)
			system('cls')
			admin()
		except:
			print("Password already exists try again !!!!")
			sleep(2)
			system('cls')
			admin()
	elif ch=='7':
		val=int(input("Enter the administrator ID: "))
		q='''SELECT admId FROM Admin'''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		x=[]
		for i in range(len(data)):
			x.append(data[i][0])
		if val in x:
			system('cls')
			l=[val]
			q='''DELETE FROM Admin WHERE admId=?'''
			BankCus.execute(q,tuple(l))
			BankCon.commit()
			x="RM_"+str(val)
			l.append(x)
			today = DT.date.today()
			s=str(today)
			l.append(s)
			t = time.localtime()
			current_time = time.strftime("%H:%M:%S", t)
			l.append(current_time)
			q='''INSERT INTO Logs (flag,lDate,lTime) VALUES (?,?,?)'''
			BankCus.execute(q,tuple(l))
			BankCon.commit()
			print("RECORD DELETED SUCCESSFULLY!")
			ch=gp.getpass("Press ENTER to CONTINUE")
			system('cls')
			admin()
		else:
			print("Enter a valid accountant ID!!!")
			sleep(2)
			system('cls')
			admin()
		system('cls')
		admin()
	elif ch=='8':
		print()
		aid=""
		while True:
			aid=input("ENTER YOUR ID: ")
			if aid.isdigit()==True:
				break
			else:
				print("ENTER A VALID ADMINISTRATOR ID !!!")
		pas=gp.getpass("ENTER NEW PASSWORD: ")
		q='''UPDATE Admin
		SET APass=?
		WHERE admId=?'''
		BankCus.execute(q,[pas,aid])
		BankCon.commit()
		print("RECORD UPDATED SUCCESSFULLY")
		sleep(2)
		system('cls')
		admin()
	elif ch=='9':
		system('cls')
		q='''SELECT * FROM Logs'''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		if len(data)==0:
			print("DO SOMETHING IN YOUR BANK TO SEE ITS LOGS!!!")
			sleep(2)
			system('cls')
			admin()
		x=PT.PrettyTable(["LOG ID","TRANSACTION ID","ACCOUNTANT ID","USER ID","FLAG","DATE","TIME"])
		for i in data:
			x.add_row(list(i))
		print(x)
		gp.getpass("PRESS ENTER TO CONTINUE")
		system('cls')
		admin()
	elif ch=='10':
		system('cls')
		q='''SELECT * FROM trans'''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		if len(data)==0:
			print("DO SOME TRANSACTIONS BEFORE VIEWING THEM!!!")
			sleep(2)
			system('cls')
			admin()
		x=PT.PrettyTable(["TRANSACTION ID","USER ID","ACCOUNTANT ID","INITIAL AMT","AMT CR/DB","CREDIT/DEBIT","BALANCE","DATE","TIME"])
		for i in data:
			x.add_row(list(i))
		print(x)
		gp.getpass("PRESS ENTER TO CONTINUE")
		system('cls')
		admin()
	elif ch=='11':
		system('cls')
		menu()
	else:
		print("ENTER A VALID CHOICE !!!")
		sleep(2)
		system('cls')
		admin()

def AccNumGen():
	n=rnd.randrange(1111,10000,1)
	num="ICICI"+str(n)
	Anum=[]
	Anum.append(num)
	q = ''' SELECT U_AccNum FROM User WHERE U_AccNum == ? '''
	temp=BankCus.execute(q,Anum)
	flag=temp.fetchone()
	check=0
	while True:
		if flag is None:
			check=1
			break
		else:
			n=rnd.randrange(1111,10000,1)
			num="ICICI"+str(n)
			Anum=[]
			Anum.append(num)
			q = ''' SELECT U_AccNum FROM User WHERE U_AccNum == ? '''
			temp=BankCus.execute(q,Anum)
			flag=temp.fetchone()
	return Anum

def DobCheck(dob):
	temp=0
	if len(dob)<10 or len(dob)>10 or dob[4]!="-" or dob[7]!="-":
		return temp
	year=int(dob[0:4])
	month=int(dob[5:7])
	day=int(dob[8:])
	if day<1:
		return temp
	elif month not in range(1,13):
		return temp
	elif year<1900 or year>2002:
		return temp
	else:
		if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)) and month == 2:
			if day>29:
				return temp
			else:
				temp=1
				return temp
		elif month==2:
			if day>28:
				return temp
			else:
				temp=1
				return temp
		elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
			if day>31:
				return temp
			else:
				temp=1
				return temp
		else:
			temp=1
			return temp

def EditAcct(opt):
	global AcId
	if opt == 1:#Create new account 
		l=[]
		l.append(AcId[0])
		while True:#Customer Name
			val=input("ENTER CUSTOMER NAME: ")
			flag=NameCheck(val)
			if flag==1:
				break
			else:
				print("Enter a valid name!!!")			
		l.append(val)
		while True:#Gender
			val=input("ENTER THE GENDER(M/F/O): ")
			if val=='M' or val=='F'or val=='O':
				l.append(val)
				break
			else:
				print("Enter a valid OPTION !!!")
		while True:#Date Of Birth
			dob=input("ENTER CUSTOMER DATE OF BIRTH(YYYY-MM-DD): ")
			flag=DobCheck(dob)
			if flag==1:
				break
			else:
				print("Enter a valid DOB!!")
		age=DT.datetime.now().year-int(dob[0:4])#Age
		l.append(age)
		while True:#Father Name
			val=input("ENTER CUSTOMER FATHER NAME: ")
			flag=NameCheck(val)
			if flag==1:
				break
			else:
				print("Enter a valid name!!!")
		l.append(val)
		l.append(dob)
		while True:#Mobile Number
			val=input("ENTER CUSTOMER MOBILE NUMBER: ")
			q='''SELECT U_Mobile FROM User WHERE U_Mobile=?'''
			heap=BankCus.execute(q,[val])
			data=heap.fetchone()
			if not data:
				if val.isdigit()==True and len(val)==10:
					l.append(int(val))
					break
				else:
					print("ENTER A VALID PHONE NUMBER!!!!")
			else:
				print("ENTER A VALID PHONE NUMBER!!!!")
		val=AccNumGen()#Account Number
		An=val
		s=val[0]
		l.append(s)
		while True:#Balance Deposited
			val=input("ENTER STARTING BALANCE DEPOSITED: ")
			if val.isdigit()==True and int(val)>5000:
				l.append(int(val))
				break
			else:
				print("THE BALANCE BEING DEPOSITED IS NOT ACCORDING TO BANK STANDARDS !!!!")
		q='''INSERT INTO User(AId,U_Name,U_Gender,U_Age,U_Fname,U_DOB,U_Mobile,U_AccNum,U_Balance) VALUES (?,?,?,?,?,?,?,?,?)'''
		BankCus.execute(q,tuple(l))
		BankCon.commit()
		q='''SELECT UserId FROM User WHERE U_AccNum LIKE ?'''#Maintaining Logs
		heap=BankCus.execute(q,(An))
		data=heap.fetchone()
		l=[]
		l.append(AcId[0])
		l.append(data[0])
		l.append("Na")
		today = DT.date.today()
		s=str(today)
		l.append(s)
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		l.append(current_time)
		q='''INSERT INTO Logs (aId,uId,flag,lDate,lTime) VALUES (?,?,?,?,?)'''
		BankCus.execute(q,tuple(l))
		BankCon.commit()
		print("NEW ACCOUNT CREATED SUCCESSFULLY")
		sleep(2)
	elif opt == 2:#Add balance in account
		print()
		q='''SELECT U_AccNum FROM User '''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		Anum=""
		while True:
			Anum=input("ENTER THE ACCOUNT NUMBER: ")
			if (Anum,) in data:
				break
			else:
				print("ENTER A VALID ACCOUNT NUMBER !!!")
		while True:
			val=input("ENTER THE AMOUNT TO BE DEPOSITED: ")
			if val.isdigit()==True:
				bal=int(val)
				break
			else:
				print("ENTER A VALID AMOUNT !!!!")
		q='''SELECT U_Balance FROM User WHERE U_AccNum like ?'''
		heap=BankCus.execute(q,[Anum])
		ini=heap.fetchone()
		Amt=ini[0]+bal
		q='''UPDATE User 
			 SET U_Balance=?
			 WHERE U_AccNum like ?
		'''
		BankCus.execute(q,[Amt,Anum])
		BankCon.commit()
		#Transaction
		T=[]
		q='''SELECT UserId FROM User WHERE U_AccNum LIKE ?'''
		heap=BankCus.execute(q,[Anum])
		data=heap.fetchone()
		T.append(data[0])
		T.append(AcId[0])
		T.append(ini[0])
		T.append(bal)
		T.append("CR")
		T.append(Amt)
		today = DT.date.today()
		T.append(str(today))
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		T.append(current_time)
		q='''INSERT INTO trans (UId,AId,initial,Amt,flag,Balance,TransDate,TransTime) VALUES (?,?,?,?,?,?,?,?)'''
		BankCus.execute(q,tuple(T))
		BankCon.commit()
		#Logs
		q='''SELECT TransId from trans WHERE AId=? and UId=? and TransDate=? and TransTime=?'''
		heap=BankCus.execute(q,[AcId[0],data[0],str(today),current_time])
		l=[]
		TId=heap.fetchone()
		l.append(TId[0])
		l.append(AcId[0])
		l.append(data[0])
		l.append("CR")
		l.append(str(today))
		l.append(current_time)
		q='''INSERT INTO Logs (tId,aId,uId,flag,lDate,lTime) VALUES (?,?,?,?,?,?)'''
		BankCus.execute(q,l)
		BankCon.commit()
		print("AMOUNT CREDITED SUCCESSFULLY")
		sleep(2)
	else:#Withdraw Balance from account
		print()
		q='''SELECT U_AccNum FROM User '''
		heap=BankCus.execute(q)
		data=heap.fetchall()
		while True:
			Anum=input("ENTER THE ACCOUNT NUMBER: ")
			if (Anum,) in data:
				break
			else:
				print("ENTER A VALID ACCOUNT NUMBER !!!")
		q='''SELECT U_Balance FROM User WHERE U_AccNum like ?'''
		heap=BankCus.execute(q,[Anum])
		ini=heap.fetchone()
		Amt=ini[0]
		while True:
			val=input("ENTER THE AMOUNT TO BE WITHDRAWN: ")
			if val.isdigit()==True and int(val)<=Amt:
				bal=int(val)
				break
			else:
				print("ENTER A VALID AMOUNT !!!!")
		Amt-=bal
		q='''UPDATE User 
			 SET U_Balance=?
			 WHERE U_AccNum like ?
		'''
		BankCus.execute(q,[Amt,Anum])
		BankCon.commit()
		#Transaction
		T=[]
		q='''SELECT UserId FROM User WHERE U_AccNum LIKE ?'''
		heap=BankCus.execute(q,[Anum])
		data=heap.fetchone()
		T.append(data[0])
		T.append(AcId[0])
		T.append(ini[0])
		T.append(bal)
		T.append("DB")
		T.append(Amt)
		today = DT.date.today()
		T.append(str(today))
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		T.append(current_time)
		q='''INSERT INTO trans (UId,AId,initial,Amt,flag,Balance,TransDate,TransTime) VALUES (?,?,?,?,?,?,?,?)'''
		BankCus.execute(q,tuple(T))
		BankCon.commit()
		#Logs
		q='''SELECT TransId from trans WHERE AId=? and UId=? and TransDate=? and TransTime=?'''
		heap=BankCus.execute(q,[AcId[0],data[0],str(today),current_time])
		l=[]
		TId=heap.fetchone()
		l.append(TId[0])
		l.append(AcId[0])
		l.append(data[0])
		l.append("DB")
		l.append(str(today))
		l.append(current_time)
		q='''INSERT INTO Logs (tId,aId,uId,flag,lDate,lTime) VALUES (?,?,?,?,?,?)'''
		BankCus.execute(q,l)
		BankCon.commit()
		print("AMOUNT DEBITED SUCCESSFULLY")
		sleep(2)

def acct():
	system('cls')
	print('''
			WELCOME TO ICICI BANK

		1) NEW ACCOUNT
		2) ADD BALANCE
		3) WITHDRAW BALANCE
		4) TRANSACTIONS
		5) ACCOUNT DETAILS
		6) LOGOUT
		''')
	ch=input("ENTER YOUR CHOICE: ")
	if ch == "1":
		EditAcct(1)
		system('cls')
		acct()
	elif ch == "2":
		EditAcct(2)
		system('cls')
		acct()
	elif ch == "3":
		EditAcct(3)
		system('cls')
		acct()
	elif ch == "4":
		print()
		Anum=input("ENTER THE ACCOUNT NUMBER: ")
		system('cls')
		q='''
		SELECT TransId as TRANSACTION_NUMBER,
		AcctName as ACCOUNTANT_NAME,
		U_Name as NAME,
		U_AccNum as ACCOUNT_NUMBER,
		initial as Balance_Initial,
		Amt as Amount,
		flag as CRedit_DeBit,
		Balance as Final_Balance,
		TransDate as Transaction_Date,
		TransTime as Transaction_Time 
		FROM trans INNER JOIN Acct on trans.AId=Acct.AcctId INNER JOIN User on trans.UId=User.UserId 
		where ACCOUNT_NUMBER like ?'''
		heap=BankCus.execute(q,[Anum])
		data=heap.fetchall()
		if len(data)==0:
			print("ENTER CORRECT ACCOUNT NUMBER !!!")
			gp.getpass("PRESS ENTER TO CONTINUE")
			system('cls')
			acct()
		x=PT.PrettyTable(["TRANS. NO.","ACCOUNTANT NAME","NAME","ACCOUNT NO.","INITIAL BAL.","AMT","FLAG","FINAL BAL.","TRANS. DATE","TRANS. TIME"])
		for i in data:
			x.add_row(list(i))
		print(x)
		gp.getpass("PRESS ENTER TO CONTINUE")
		system('cls')
		acct()
	elif ch == "5":
		print()
		Anum=input("ENTER THE ACCOUNT NUMBER: ")
		system('cls')
		q='''SELECT U_AccNum,U_Name,U_Gender,U_FName,U_DOB,U_Mobile FROM User WHERE U_AccNum like ?'''
		heap=BankCus.execute(q,[Anum])
		data=heap.fetchone()
		if data==None:
			print("ENTER CORRECT ACCOUNT NUMBER !!!")
			gp.getpass("PRESS ENTER TO CONTINUE")
			system('cls')
			acct()
		else:
			print("\t\t\tACCOUNT DETAILS\n")
			print("ACCOUNT NUMBER: ",data[0])
			print("          NAME: ",data[1])
			print("        GENDER: ",data[2])
			print("   FATHER NAME: ",data[3])
			print(" DATE OF BIRTH: ",data[4])
			print(" MOBILE NUMBER: ",data[5])
			gp.getpass("\n\n\nPRESS ENTER TO CONTINUE")
			system('cls')
			acct()
	elif ch == "6":
		system('cls')
		menu()
	else:
		print("ENTER A VALID OPTION!!!!")
		sleep(2)
		acct() 

def login(auth):#login check for administrator and accountant
	global AdId
	global AcId
	if auth == 'admin':
		system('cls')
		l=[]
		name=input('Enter your name: ')
		pwd=gp.getpass("Enter your password: ")
		l.append(name)
		l.append(pwd)
		q=''' SELECT AName,APass FROM Admin WHERE AName=? AND APass=?'''
		heap=BankCus.execute(q,tuple(l))
		data=heap.fetchone()
		if data is None:
			print("NO RECORD FOUND !!!!!")
			sleep(2)
			system('cls')
			menu()
		elif data[0]==name and data[1]==pwd:
			q='''SELECT admId FROM Admin WHERE AName=? AND APass=?'''
			heap=BankCus.execute(q,(name,pwd))
			AdId=heap.fetchone()
			admin()
		else:
			print("Try again with correct credentials")
			sleep(2)
			system('cls')
			menu()
	else:
		system('cls')
		l=[]
		name=input('Enter your name: ')
		pwd=gp.getpass("Enter your password: ")
		l.append(name)
		l.append(pwd)
		q=''' SELECT AcctName,AcctPass FROM Acct WHERE AcctName=? AND AcctPass=?'''
		heap=BankCus.execute(q,tuple(l))
		data=heap.fetchone()
		if data is None:
			print("NO RECORD FOUND !!!!!")
			sleep(2)
			system('cls')
			menu()
		elif data[0]==name and data[1]==pwd:
			q='''SELECT AcctId FROM Acct WHERE AcctName=? AND AcctPass=?'''
			heap=BankCus.execute(q,(name,pwd))
			AcId=heap.fetchone()
			acct()
		else:
			print("Try again with correct credentials")
			sleep(2)
			system('cls')
			menu()

def menu():
	print('''
			ICICI BANK
		1) ADMINISTRATOR LOGIN
		2) ACCOUNTANT LOGIN
		3) EXIT

		''')
	ch=input("Enter your choice: ")
	if ch == '1':
		system('cls')
		login('admin')
		system('cls')
		menu()
	elif ch == '2':
		system('cls')
		login('accountant')
		system('cls')
		menu()
	elif ch == '3':
		system('cls')
		exit()
	else:
		print("Enter a valid choice !!!!")
		sleep(2)
		system('cls')
		menu()

system('cls')
menu()