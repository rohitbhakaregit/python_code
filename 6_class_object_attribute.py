class Pet():
	universal="Animal"  # class object attribute (Glaballay acciable )

	def __init__(self,name, color ):
		self.color=color
		self.name=name 
	def bark(self):
		print("aauuuuuuuuuuuuuuuuuu  {}".format(self.name))
p= Pet("Nishant","Black")

print(p.color)
print(p.name)
print(p.universal)
p.bark()




