# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))
# from datetime import date

# import datetime as DT
# today = DT.date.today()
# s=str(today)
# print("Today's date:", s,"",today,type(today))

# import time
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time,type(current_time))

# import datetime as DT
# now = DT.datetime.now().year
# print(now)
# import sqlite3 as sql
# import random as rnd 
# BankCon=sql.connect("bank.db")# owner of the bank
# BankCus=BankCon.cursor()
# n=rnd.randrange(1111,10000,1)
# num="ICICI"+str(n)
# print(num)
# Anum=[]
# Anum.append(num)
# print(Anum)
# q = ''' SELECT U_AccNum FROM User WHERE U_AccNum == ? '''
# a=BankCus.execute(q,Anum)
# data=a.fetchone()
# if data is None:
# 	print("yes")
# else:
# 	print("false")
# dob="1995-12-25"
# def DobCheck(dob):
# 	year=int(dob[0:4])
# 	month=int(dob[5:7])
# 	day=int(dob[8:])
# DobCheck(dob)
# x=1
# if x in range(1,13):
# 	print("True")
# x="02"
# y=int(x)
# if y==2:
# 	print("yes")
# import re 
  
# def validating_name(name): 
  
#     # RegexObject = re.compile( Regular expression, flag ) 
#     # Compiles a regular expression pattern into a regular expression object 
#     regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',  
#               re.IGNORECASE) 
  
#     # RegexObject is matched with the desired  
#     # string using search function 
#     # In case a match is found, search() returns 
#     # MatchObject Instance 
#     # If match is not found, it return None 
#     res = regex_name.search(name) 
  
#     # If match is found, the string is valid 
#     if res: print("Valid") 
          
#     # If match is not found, string is invalid 
#     else: print("Invalid") 
  
# # Driver Code 
# validating_name('Mr. Albus Severus Potter') 
# validating_name('Lily and Mr. Harry Potter') 
# validating_name('Mr. Cedric') 
# validating_name('sirius black') 
# x="123456789"
# y=int(x)
# print(len(x))
import sqlite3 as sql
BankCon=sql.connect("bank.db")
BankCus=BankCon.cursor()
# q='''SELECT U_AccNum FROM User '''
# heap=BankCus.execute(q)
# data=heap.fetchall()
# if ("ICICI9159",) in data:
# 	print(data,type(data))
print("+----------------------------------+------------------------------+")
print("|                                  |                              |")
print("+----------------------------------+------------------------------+")