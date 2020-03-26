"""object creatioin 
class demo :
	x=100

d= demo()
print (d.x) """


#calling init 

class pen:
	def __init__(self, color ,size , ptype):
		self.color=color
		self.size=size
		self.ptype=ptype

p1=pen("red","7","jel")

print("pen color ="+p1.color+"\n"+"pen size ="+p1.size+"\n"+"pen type="+p1.ptype)


