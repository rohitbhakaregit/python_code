try:
	fi=open("ramchan.txt","r")
	fi.write("kudi appa pa pa ....")
	fi.close()
except:
	print("Exception from read ")
	fi=open("ramchan.txt","a")
	fi.write("aja o meri tamana ")
	fi.close()
finally:
	print("finally")
	fi=open("ramchan.txt","r")
	print(fi.read())
	fi.close()