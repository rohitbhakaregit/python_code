class Account():
	def __init__(self, person_name, balance):
		self.person_name=person_name
		self.balance=balance
		print("Person_name: {}".format(self.person_name))
		print("Balance    : {}".format(self.balance))

	def deposit(self,amount):
		self.balance= self.balance + amount
		print("Your account balance deposited by {} /- rs ".format(amount))
		return self.balance 
	def withdrow(self,amount):
		if(self.balance-amount > 0):
			self.balance= self.balance - amount 
			print("Your account balance withdrow by {} /- rs ".format(amount))
			return self.balance
		else:
			return "insufficient balance"

bal=input("enter the defalult Acoount  balance :")
a=Account("Rohit",int(bal))

while temp!=4:
	ans=input("do you want to deposit/withdrow  (D/W)")
	if ans == 'W':
		wamt=input("Enter amount to withdrow")
		print ("Account balance : {}".format(a.withdrow(int(wamt))))
	elif ans == 'D':
		aamt=input("Enter amount to deposit")
		print ("Account balance : {}".format(a.deposit(int(aamt))))
	temp=temp+1
