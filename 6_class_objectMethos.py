"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

"""

class ObjectMethod :
	def __init__(self, arg1, arg2):
		self.arg1=arg1
		self.arg2=arg2
	
	def ObjectFunction(self,local):   ## here you can use anything in the replacemnt for self
		print("Argumetn1="+self.arg1)  
		print("Argumetn2="+self.arg2)
		print("local=>"+local)

   
	def ObjectFunction1(sel):   ## here you can use anything in the replacemnt for self 
		print("Argumetn1="+sel.arg1)  
		print("Argumetn2="+sel.arg2)
		#modify the parameter 
		sel.arg1 =sel.arg1+sel.arg2
		print("modified object=>"+sel.arg1)



om=ObjectMethod("haha","hihi")
om.ObjectFunction("localarg")
om.ObjectFunction1()

