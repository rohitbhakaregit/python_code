import math 
class line():
	def __init__(self,cordinate1,cordinate2):
		self.x1=cordinate1[0]
		self.y1=cordinate1[1]
		self.x2=cordinate2[0]
		self.y2=cordinate2[1]
	def distance(self):
		return math.sqrt((self.x2 -self.x1)**2 + (self.y2- self.y1)**2)
	def slop(self):
		return  (self.y2-self.y1)/(self.x2-self.x1)
l=line((3,2),(8,10))
print (l.distance())
print (l.slop())