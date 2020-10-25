import pickle as p
def reset():	
	file=open("admin.txt","wb")
	p.dump({"1":["Vaibhav","1234",]},file)
	file.close()
	file=open("cab.txt","wb")
	p.dump({},file)
	file.close()
	file=open("user.txt","wb")
	p.dump({},file)
	file.close()
	file=open("dealer.txt","wb")
	p.dump({},file)
	file.close()