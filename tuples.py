tup=("carrot","sweetpotato","bringle","fenugreek","carrot","carrot")  #tuples defined inside

"""tup[1]="gajar"  TypeError: 'tuple' object does not support item assignment"""


for x in tup:
	print(x)


if "fenugreek" in tup:
	print("yes!")


print(len(tup))          # print tuple length

print("count:" , tup.count("carrot"))                      # print how many times the specified value gets repetated 

print("index:" ,tup.index("bringle"))                      # print the item position 
#print( tup [1])








