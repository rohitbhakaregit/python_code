"""
# exe3 : list down the words that start 's' with using split()
str1="This is Rohit & you are wathing to super shuman sSSA Cert sSSS"

for words in str1.split():
	if words.startswith('s'):
		print words

for words in str1.split():
	if words[0]=='s':
		print words
# exe 2:print out the even number 0 to 10  

for i in range(0,10):
	if i % 2==0:
		print i

# exe 3 : list comprehension print number 1 to 50 divisible by 3 

for i in range(1,1000):
	num = i
	print [list1 for list1 in range(num, num*11) if list1 % num == 0]


#exe 4: print event lenght string 


string=" help to other god will help you"
for s in string.split():
	if len(s)%2==0:
		print s

#exe5: print 1-10  divisible by 3 replace by FIZZ & %5 BuZZ & both FIZZBUZZ
for i in range(1,101):
	if i%3==0 and i%5==0:
		print "FIZZBUZZ"
	if i%3==0:
		print "FIZZ"
	elif i%5==0:
		print "BUZZ"
	else:
		print i

		"""

# list comprehension with print fist letter in string 
fsring="range other help i try"

print [words[0] for words in fsring.split()]
