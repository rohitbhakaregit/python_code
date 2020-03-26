def squre(num):
	while True:
		try:
			return num**2
		except:
			print("Exception")
			i= input("do you want to correct ?")
			if i=='y':
				print(squre(5))
				break
			else:
				continue
		else:
			print("No exception")
			continue
		finally:
			print("I am alwase run")

print(squre('5'))
#above one is my logic 


