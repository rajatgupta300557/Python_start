import pickle as p
import getpass as gp
import re as reg
from os import system
from time import sleep
import reset as res

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' # regex to verify an authentic email id

def regis(fname):#list store format {"id":[Name,phone no, email, password]}
	d={}
	l=[]
	temp=0
	file=open(fname,"rb")
	d=p.load(file)
	file.close()
	file=open(fname,"wb")
	s = input("Enter your Name: ")
	l.append(s)#name added to list
	
	if (not bool(d) == True):
		while True:
			s = input("Enter your mobile number: ")
			if s.isnumeric()==True:
				l.append(s)#phone number added
				break
			else:
				print("Enter a valid phone number!")
	else:
		while True:
			s = input("Enter your mobile number: ")
			if s.isnumeric()==True:
				for i in d.values():
					if s not in i[1]:
						temp=1
						break
					else:
						print("Enter a valid phone number of yours")
						break
				if temp==1:
					temp=0
					break
				else:
					continue
			else:
				print("Enter a valid phone number of yours")
		l.append(s)#phone number added
	
	if (not bool(d) == True):
		while True:
			s = input("Enter your email: ")
			if(reg.search(regex,s)):
				l.append(s)#email added
				break
			else:
				print("Enter a valid E-mail!")
	else:
		while True:
			s = input("Enter your email: ")
			if(reg.search(regex,s)):
				for i in d.values():
					if s not in i[2]:
						temp=1
						break
					else:
						print("Email already exist enter a valid email!")
						break
				if temp == 1:
					temp=0
					break
				else:
					continue
			else:
				print("Enter a valid E-mail !!!")
		l.append(s)#email added

	s = gp.getpass("Enter your password: ")
	l.append(s)#password added
	if (not bool(d) == True):#if it is first record added
		d["1"]=l
		p.dump(d,file)
		file.close()
		for i in range(65):
			print("-",end="")
		print()
		print("|{0:^15}|{1:^15}|{2:^15}|{3:^15}|".format("ID","Name","Phone Number","Email"))
		for i in range(65):
			print("-",end="")
		print()
		print("|{0:^15}|{1:^15}|{2:^15}|{3:^15}|".format("1",d["1"][0],d["1"][1],d["1"][2]))
		for i in range(65):
			print("-",end="")
		print()
		k=gp.getpass("Press enter to continue")
		system('cls')
	else:
		q=d.keys()
		t=list(q)
		k=int(t[-1])
		k+=1 
		d[str(k)]=l
		p.dump(d,file)
		file.close()
		for i in range(65):
			print("-",end="")
		print()
		print("|{0:^15}|{1:^15}|{2:^15}|{3:^15}|".format("ID","Name","Phone Number","Email"))
		for i in range(65):
			print("-",end="")
		print()
		print("|{0:^15}|{1:^15}|{2:^15}|{3:^15}|".format(str(k),d[str(k)][0],d[str(k)][1],d[str(k)][2]))
		for i in range(65):
			print("-",end="")
		print()
		ch=gp.getpass("Press enter to continue")
		system('cls')

def userReg():
	system('cls')
	regis("user.txt")
	system('cls')
	menu()

def dealerReg(): 
	system('cls')
	regis("dealer.txt")
	system('cls')
	menu()

def cabOpt(n,Id="",fname=""): # for 1 add a new cab; 2 view all cabs; 3 update cabs; 4 delete a cab
	global Did
	dC={}
	l=[]
	file=open("cab.txt","rb")
	dC=p.load(file)
	file.close()#saving the content of cab file
	if n == 1 : #new cab format{"id":[d id,dealer name,cab name, type(wheeler),model(car bike van auto royal), cab number,from, to]}
		dD={}
		fdeal=open("dealer.txt","rb")# using dealer file to take dealer id and dealer name
		dD=p.load(fdeal)
		fdeal.close()
		s=Id
		l.append(s)
		l.append(dD[s][0])
		s = input("Enter the cab name: ")
		l.append(s)
		s = input("Enter the cab type: ")
		l.append(s)
		s = input("Enter the cab model: ")
		l.append(s)
		s = input("Enter the cab number: ")
		l.append(s)
		s = input("Cab from: ")
		l.append(s)
		s = input("Cab to: ")
		l.append(s)
		if (not bool(dC) == True):
			dC["1"]=l
			fcab=open("cab.txt","wb")
			p.dump(dC,fcab)
			fcab.close()
		else:
			q=dC.keys()
			t=list(q)
			k=int(t[-1])
			k+=1 
			dC[str(k)]=l
		fcab=open("cab.txt","wb")
		p.dump(dC,fcab)
		fcab.close()
		print()
		#cabOpt(2,s)
		system('cls')
	elif n == 2 :#view all cab
		file=open("cab.txt","rb")
		d=p.load(file)
		file.close()
		if (not bool(dC) == True):
			print("No cabs available")
			ch=gp.getpass("Press enter to continue")
		elif fname=="dealer.txt":
			Id=Did
			for i in range(134):
				print("-",end="")
			print()
			print("|{0:^8}|{1:^11}|{2:^15}|{3:^15}|{4:^15}|{5:^10}|{6:^20}|{7:^15}|{8:^15}|".format("CabID","Dealer_Id","Dealer Name","Cab Name","Type","Model","Registeration Number","From","To"))
			for i in range(134):
				print("-",end="")
			print()
			for i in dC.keys():
				if dC[i][0]==Id:
					print("|{0:^8}|{1:^11}|{2:^15}|{3:^15}|{4:^15}|{5:^10}|{6:^20}|{7:^15}|{8:^15}|".format(i,d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]))
					for i in range(134):
						print("-",end="")
					print()
			ch=gp.getpass("Press enter to continue")
		else:
			for i in range(134):
				print("-",end="")
			print()
			print("|{0:^8}|{1:^11}|{2:^15}|{3:^15}|{4:^15}|{5:^10}|{6:^20}|{7:^15}|{8:^15}|".format("CabID","Dealer_Id","Dealer Name","Cab Name","Type","Model","Registeration Number","From","To"))
			for i in range(134):
				print("-",end="")
			print()
			for i in dC.keys():
				print("|{0:^8}|{1:^11}|{2:^15}|{3:^15}|{4:^15}|{5:^10}|{6:^20}|{7:^15}|{8:^15}|".format(i,d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7]))
				for i in range(134):
					print("-",end="")
				print()
			ch=gp.getpass("Press enter to continue")
	elif n == 3 :#update cab
		fcab=open("cab.txt","rb")
		dC=p.load(fcab)
		fcab.close()
		fdeal=open("dealer.txt","rb")
		dD=p.load(fdeal)
		fdeal.close()
		Cid=input("Enter the cab id: ")
		if Cid in dC.keys():
			l.append(Did)
			l.append(dD[Did][0])
			s = input("Enter the cab name: ")
			l.append(s)
			s = input("Enter the cab type: ")
			l.append(s)
			s = input("Enter the cab model: ")
			l.append(s)
			s = input("Enter the cab number: ")
			l.append(s)
			s = input("Cab from: ")
			l.append(s)
			s = input("Cab to: ")
			l.append(s)
			fcab=open("cab.txt","wb")
			dC[Cid]=l
			p.dump(dC,fcab)
			fcab.close()
			print("Record Updated !")
			sleep(2)
			system('cls')
		else:# check for invalid cab id
			print("Enter a valid cab id !!!")
			sleep(2)
			system('cls')
	elif n == 4:#delete a cab
		system('cls')
		file=open("cab.txt","rb")
		dC=p.load(file)
		file.close()
		if (not bool(dC) == True):
			print("No cabs to be deleted")
			ch=gp.getpass("Press enter to continue..")
		elif fname=="admin.txt":
			file=open("dealer.txt","rb")
			d=p.load(file)
			file.close()
			ch=input("Enter the cab ID to be deleted: ")
			if ch in dC.keys():
				dC.pop(ch)
				file=open("cab.txt","wb")
				p.dump(dC,file)
				file.close()
			else:
				file.close()
				print("Enter a correct cab ID !!!")
				ch=gp.getpass("Press enter to continue")
		else:
			file=open("dealer.txt","rb")
			d=p.load(file)
			file.close()
			if Id in d.keys():
				ch=input("Enter the cab ID to be deleted: ")
				if dC[ch][0]==Id:
					dC.pop(ch)
					file=open("cab.txt","wb")
					p.dump(dC,file)
					file.close()
				else:
					file.close()
					print("Enter a correct cab ID !!!")
					ch=gp.getpass("Press enter to continue")
			else:
				print("Enter a valid ID")
				k=gp.getpass("Press enter to continue")

def dealerLog(flag=0):
	global Did
	if flag == 0: #dealer login should work only once that is why flag is set to zero
		system('cls')
		file = open("dealer.txt","rb")
		d=p.load(file)
		file.close()
		if (not bool(d) == True):
			print("Register yourself before you login")
			ch=gp.getpass("Press enter to continue")
			system('cls')
			menu()
		else:
			name=input("Enter your name: ")
			passw=gp.getpass("Enter your password: ")
			for i in d.keys():
				if(d[i][0] == name and d[i][-1]==passw):
					Did=i
					flag=1
					break
			if flag==0:
				print("Enter the correct username and password !!!")
				sleep(2)
				system('cls')
				menu()
	system('cls')
	print('''
		DEALER SERVICES

	1) ADD CABS
	2) VIEW CABS 
	3) UPDATE CABS
	4) DELETE CAB
	5) UPDATE PROFILE
	6) CHANGE PASSWORD
	7) LOGOUT

	''')
	ch=input("Enter your choice: ")
	if ch == '1' :
		cabOpt(1,Did)
		dealerLog(1)
	elif ch == '2' :
		cabOpt(2,Did,"dealer.txt")
		dealerLog(1)
	elif ch == '3' :
		cabOpt(3,Did)
		dealerLog(1)
	elif ch == '4' :
		cabOpt(4,Did)
		dealerLog(1)
	elif ch == '5' :
		system('cls')
		profUp("dealer.txt")
		dealerLog(1)
	elif ch == '6':
		system('cls')
		chanPass("dealer.txt",Did)
		dealerLog(1)
	elif ch =='7':
		system('cls')
		menu()
	else :
		print("Enter an appropriate choice !!!!")
		k=gp.getpass("Press enter to continue")
		system('cls')
		dealerLog(1)

def searchCab():# this search is based on the cabID 
	system('cls')
	fcab=open("cab.txt","rb")
	d=p.load(fcab)
	ch=input("Enter the cabID to be searched: ")
	if ch in d.keys():
		for i in range(102):
			print("-",end="")
		print()
		print("|{0:^8}|{1:^11}|{2:^15}|{3:^15}|{4:^15}|{5:^10}|{6:^20}|".format("CabID","Dealer_Id","Dealer Name","Cab Name","Type","Model","Registeration Number"))
		for j in range(102):
			print("-",end="")
		print()
		print("|{0:^8}|{1:^11}|{2:^15}|{3:^15}|{4:^15}|{5:^10}|{6:^20}|".format(ch,d[ch][0],d[ch][1],d[ch][2],d[ch][3],d[ch][4],d[ch][5]))
		for j in range(102):
			print("-",end="")
		print()
		temp=gp.getpass("")
		fcab.close()
	else:
		i=3
		while i>0:
			system('cls')
			print("Either the cabID is wrong or the record does not exist try again in ",i)
			i-=1
			sleep(1)
		fcab.close()
		searchCab()

def profUp(fname):
	system('cls')
	ch = input("Enter your ID: ")
	file=open(fname,"rb")
	dU=p.load(file)
	file.close()
	if ch in dU.keys():
		fuser=open(fname,"wb")
		l=[]
		s = input("Enter your Name: ")
		l.append(s)
		while True:
			s = input("Enter your mobile number: ")
			if s.isnumeric()==True:
				for i in dU.values():
					if s not in i[1]:
						temp=1
						break
					else:
						print("Enter a valid phone number of yours")
						break
				if temp==1:
					temp=0
					break
				else:
					continue
			else:
				print("Enter a valid phone number of yours")
		l.append(s)#phone number added
		while True:
			s = input("Enter your email: ")
			if(reg.search(regex,s)):
				for i in dU.values():
					if s not in i[2]:
						temp=1
						break
					else:
						print("Email already exist enter a valid email!")
						break
				if temp == 1:
					temp=0
					break
				else:
					continue
			else:
				print("Enter a valid E-mail !!!")
		l.append(s)#email added
		s = gp.getpass("Enter your password: ")# check for pre existing passwords
		l.append(s)
		dU[ch]=l
		p.dump(dU,fuser)
		fuser.close()
		k=gp.getpass("Profile Updated \nPress enter to continue")
		system('cls')
	else:
		print("Wrong ID entered !!!")
		sleep(2)
		system('cls')

def chanPass(fname,Id=""):
	system('cls')
	#ch = input("Enter your ID: ")
	fuser=open(fname,"rb")
	dU=p.load(fuser)
	fuser.close()
	if Id in dU.keys():	
		npass=gp.getpass("Enter your new password: ")
		npass1=gp.getpass("Confirm your password: ")
		if npass==npass1:
			fuser=open(fname,"wb")
			dU[Id][-1]=npass
			p.dump(dU,fuser)
			fuser.close()
			print("Password Updated !!")
			sleep(1)
			system('cls')
		else:
			print("Passwords did not match !!")
			sleep(2)
			system('cls')
	else:
		print("Wrong ID entered !!")
		sleep(2)
		system('cls')
		chanPass()

def userLog(flag=0):
	global Uid
	if flag == 0: #user login should work only once that is why flag is set to zero
		system('cls')
		file = open("user.txt","rb")
		d=p.load(file)
		file.close()
		if (not bool(d) == True):
			print("Insert some records to be viewed")
			ch=gp.getpass("Press enter to continue")
			system('cls')
			menu()
		else:
			name=input("Enter your name: ")
			passw=gp.getpass("Enter your password: ")
			for i in d.keys():
				if(d[i][0] == name and d[i][-1]==passw):
					Uid=i
					flag=1
					break
			if flag==0:
				print("Enter the correct username and password !!!")
				sleep(2)
				system('cls')
				menu()
	system('cls')
	print('''
		USER SERVICES

	1) VIEW ALL CABS
	2) SEARCH CABS 
	3) UPDATE PROFILE
	4) CHANGE PASSWORD
	5) EXIT

	''')
	ch=input("ENTER YOUR CHOICE: ")
	if ch =='1':
		system('cls')
		cabOpt(2)
		userLog(1)
	elif ch == '2':
		system('cls')
		searchCab()
		userLog(1)
	elif ch == '3':
		system('cls')
		profUp("user.txt")
		userLog(1)
	elif ch == '4':
		system('cls')
		chanPass("user.txt",Uid)
		userLog(1)
	elif ch == '5':
		system('cls')
		menu()
	else:
		print("Enter a valid input !!!")
		ch = gp.getpass("Press enter to continue")
		userLog(1)

def details(fname):
	system('cls')
	if fname=="admin.txt":
		fadm=open("admin.txt","rb")
		dA=p.load(fadm)
		fadm.close()
		for j in range(34):
			print("-",end="")
		print()
		print("|{0:^10}|{1:^10}|{2:^10}|".format("Admin ID","Name","Password"))
		for j in range(34):
			print("-",end="")
		print()
		for i in dA.keys():
			print("|{0:^10}|{1:^10}|{2:^10}|".format(i,dA[i][0],dA[i][1]))
			for j in range(34):
				print("-",end="")
			print()
		ch=gp.getpass("Press enter to continue")
	else:
		d={}
		file=open(fname,"rb")
		d=p.load(file)
		file.close()
		if (not bool(d) == True):
			print("Insert some records to be viewed")
			ch=gp.getpass("Press enter to continue")
		else:
			for j in range(81):
				print("-",end="")
			print()
			print("|{0:^15}|{1:^15}|{2:^15}|{3:^15}|{4:^15}|".format("ID","Name","Phone Number","Email","Password"))
			for j in range(81):
				print("-",end="")
			print()
			for i in d.keys():
				print("|{0:^15}|{1:^15}|{2:^15}|{3:^15}|{4:^15}|".format(i,d[i][0],d[i][1],d[i][2],d[i][3]))
				for j in range(81):
					print("-",end="")
				print()
			ch=gp.getpass("Press enter to continue")

def rem(fname):
	file=open(fname,"rb")
	d=p.load(file)
	file.close()
	if (not bool(d) == True):
		print("There are no records to be deleted please enter a record first\nPress enter to continue")
		ch=gp.getpass("")
		system('cls')
		adminLogin(1)
	ch = input("Enter the ID to be deleted: ")
	if ch in d.keys():
		if fname=="dealer.txt":#for deleting a dealer its corresponding cabs must be deleted
			fcab=open("cab.txt","rb")
			dC = p.load(fcab)
			fcab.close()
			fdeal=open("dealer.txt","rb")
			dD=p.load(fdeal)
			fdeal.close()
			dD.pop(ch)
			key=list(dC.items())
			for i,j in key:
				if j[0]==ch:
					dC.pop(i)
			fcab=open("cab.txt","wb")
			p.dump(dC,fcab)
			fcab.close()
			fdeal=open("dealer.txt","wb")
			p.dump(dD,fdeal)
			fdeal.close()
		else:	
			d.pop(ch)
			print("Record deleted press enter to continue")
			file=open(fname,'wb')
			p.dump(d,file)
			file.close()
			ch=gp.getpass("")
			system('cls')
	else:
		print("Enter a vaild ID to be deleted")
		print("Press enter to continue")
		ch=gp.getpass("")
		system('cls')

def newAdm(flag=0):
	if flag == 0:#add new admin
		fadm=open("admin.txt","rb")
		dA=p.load(fadm)
		fadm.close()
		l=[]
		s=input("Enter Name: ")
		l.append(s)
		s=gp.getpass("Enter password: ")
		l.append(s)
		fadm=open("admin.txt","wb")
		q=dA.keys()
		t=list(q)
		k=int(t[-1])
		k+=1 
		dA[str(k)]=l
		p.dump(dA,fadm)
		print("New admin added successfully")
		fadm.close()
		system('cls')
	else: #change password for admin logged in
		l=[]
		fadm=open("admin.txt","rb")
		dA=p.load(fadm)
		fadm.close()
		ch=input("Enter your ID: ")
		if ch in dA.keys():
			s=gp.getpass("Enter new password: ")
			l.append(s)
			fadm=open("admin.txt")
			dA[ch]=l
			p.dump(dA,fadm)
			fadm.close()
		else:
			print("Enter correct admin ID\n Press enter to continue")
			ch=gp.getpass()
			adminLogin(1)

def adminLogin(flag=0): 
	Aid=""
	#admin login should work only once that is why flag is set to zero
	if flag==0:
		system('cls')
		file = open("admin.txt","rb")
		d=p.load(file)
		name=input("Enter your name: ")
		passw=gp.getpass("Enter your password: ")
		for i in d.keys():
			if(d[i][0] == name and d[i][1]==passw):
				flag=1
				Aid=i
				break
		file.close()
		if flag==0:
			print("Enter the correct username and password !!!")
			print("Press enter to continue")
			ch=gp.getpass("")
			system('cls')
			menu()
	system('cls')
	print('''
		ADMINISTRATOR SERVICES

	1)  VIEW ALL USERS
	2)  DELETE USER
	3)  VIEW ALL DEALERS 
	4)  DELETE DEALER
	5)  VIEW ALL CABS
	6)  DELETE CAB
	7)  ADD NEW ADMIN
	8)  CHANGE PASSWORD
	9)  VIEW ALL ADMIN
	10) RESET DATA
	11) UPDATE PROFILE
	12) LOGOUT

	''')
	ch=input("ENTER YOUR CHOICE: ")	
	if ch =='1':
		details("user.txt")
		adminLogin(1)
	elif ch == '2':
		rem("user.txt")
		adminLogin(1)
	elif ch == '3':
		details("dealer.txt")
		adminLogin(1)
	elif ch == '4':
		rem("dealer.txt")
		adminLogin(1)
	elif ch == '5':
		cabOpt(2)
		adminLogin(1)
	elif ch == '6':
		cabOpt(4,"","admin.txt")
		adminLogin(1)
	elif ch == '7':
		newAdm()
		adminLogin(1)
	elif ch == '8':
		newAdm(1)
		adminLogin(1)
	elif ch == '9':
		details("admin.txt")
		adminLogin(1)
	elif ch == '10':
		res.reset()
		system('cls')
		print("All data set to null and Admin made default")
		ch=gp.getpass("Press enter to continue")
		system('cls')
		adminLogin(1)
		menu()
	elif ch == '11':
		system('cls')
		f=open("admin.txt","rb")
		d=p.load(f)
		f.close()
		file=open("admin.txt","wb")
		l=[]
		s=input("Enter your name: ")
		l.append(s)
		d[Aid][0]=l[0]
		p.dump(d,file)
		file.close()
		k=gp.getpass("Press enter to continue")
		adminLogin(1)
	elif ch == '12':
		print("Logging out....")
		sleep(1)
		system('cls')
		menu()
	else:
		print("Enter a correct option !!!")
		k=gp.getpass("Press enter to continue")
		system('cls')
		adminLogin(1)

def menu():
	print('''
		CAB BOOKING SERVICES

	1) ADMIN LOGIN
	2) USER REGISTRATION 
	3) USER LOGIN
	4) DEALER REGISTERATION
	5) DEALER LOGIN
	6) EXIT

	''')
	ch=input("ENTER YOUR CHOICE: ")
	if ch == '1':
		adminLogin()
	elif ch == '2':
		userReg()
	elif ch == '3':
		userLog()
	elif ch == '4':
		dealerReg()
	elif ch=='5':
		dealerLog()
	elif ch == '6':
		exit()
	else:
		print("Enter a valid choice")
		k=gp.getpass("Press enter to continue")
		system('cls')
		menu()

system('cls')
menu() 
system('cls')