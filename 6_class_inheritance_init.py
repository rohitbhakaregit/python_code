class parent(object):
	"""docstring for parent"""
	def __init__(self, arg):
 		self.arg = arg
		print "from parent"+arg
		ok="Ramchandra"
class child(parent):
	def __init__(self,arg):
		self.arg=arg
		print "from child"+arg

c=child("--ok")
print c.ok
