"""This is the code for assigning function to variable 
you can pass the  function as parameter 
]-Rohit Bhakare """

def decorator(original_function):
	def pre():
		print("I will execute first")
	def post():
		print("I will execute last ")

	pre()
	original_function()
	post()

@decorator                                   # or use decore @ to on and off the function passing 
def origin():
	print("Here I want pre & post ")

#decorator(origin)                             # either you call devore function with referance to original function 