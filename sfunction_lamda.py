""" lambda is anonimus function wich can take any argummet but 
process onely one expression 
"""

"""

#lamda with a argument 

z = lambda a : a*10
print(z(5))


#lambda with multiple parameters 

k= lambda r, o ,h ,i ,t : r+r+o+o+h+h+i+i+t+t
print(k("ro","oh","hi","it","tt"))

"""
# lamda in function 

def cal(a):
	return lambda x: x+a


print(cal(2))
print(cal(5))