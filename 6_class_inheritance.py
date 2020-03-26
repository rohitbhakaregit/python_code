class parent :
	def __init__(self, name, surname ):
		self.name =name
		self.surname= surname

	def fun_print(self):
		print(self.name+ self.surname)



class child(parent):
	def __init__(self,name,surname):
		parent.__init__(self, name, surname)	

c=child("Rohit","bhakare")

c.fun_print()




