class temp():
	def __init__(self,bottle_name,color,liter):
		self.bottle_name =bottle_name
		self.color=color
		self.liter=liter
	#magic mthod 

	def __str__(self):   # return string method 
		return f"bottle name {self.bottle_name} of color {self.color} contain {self.liter}"
	def __len__(self):  # retuen length
		return self.liter*1000


t=temp("dr bronz","bronz",2)
print(t)		
print (len(t))