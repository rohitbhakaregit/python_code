
def add(num1,num2):

	try:
		return num1+num2
	except:
		print("Run from except")
		return int(num2)+int(num1)
	finally:
		print ("I am always execute..")

print (add(1,"3"))