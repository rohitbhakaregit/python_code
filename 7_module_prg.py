"""import module 
name=module.name_fun("anuradha")
print (name)

#import as aliase 

import module as m
print (m.name_fun("anurasha"))
"""
import platform
import random
import time
"""print (platform.node())
print (platform.processor())

v=platform.dist()
print(v[2])
"""
while 1:
	i=""
	while i !="z":
		i=random.choice(["a","b","c","d","e","f","g","h","i","z"])
		if (i=="z"):
			print("cought z........................................")
			time.sleep(5)
			break
		else:
			print(i)