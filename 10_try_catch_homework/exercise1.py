try:
	for i in ['a','b','c']:
		print(i**2)
except Exception as e:
	print("exetion while running ", e )
finally:
	print("finally running")