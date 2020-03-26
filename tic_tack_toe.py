from os import system
p1_win=0
p2_win=0

x=["-","-","-","-","-","-","-","-","-","-"]
#for i in range(0,3
print("| 9 | 8 | 7 |")
print("----------")
print("| 6 | 5 | 4 |")
print("----------")
print("| 3 | 2 | 1 |")
print("----------")


p1=input("player1 choose your character: ")
p2=input("player2 choose your character: ")

def switch(play , player):
	if (int(play)<=9 and int(player) == 1 ):
		if x[int(play)] == "-":
			x[int(play)]=p1
		else:
			p1_play=input("Player1 : Enter valid block [1-9]")
			switch(p1_play,1)
	

	elif (int(play)<=9 and int(player) == 2):
		if x[int(play)] == "-":
			x[int(play)]=p2
		else:
			p2_play=input("Player2 : Enter valid block [1-9]")
			switch(p2_play,2)

	else:
		print ("Wrong choice")
	system("clear")
	print("| {} | {} | {} |".format(x[9],x[8],x[7]))
	print("----------")
	print("| {} | {} | {} |".format(x[6],x[5],x[4]))
	print("----------")
	print("| {} | {} | {} |".format(x[3],x[2],x[1]))
	print("----------")
	win(x,p1,p2)
	

def win(x,p1,p2):
	if(x[9]==x[5]==x[1]==p1 and x[9]!="-" and x[5]!="-" and x[1]!="-" ):
		p1_win=1
		print("player1 win")
		exit(0)
		
	elif(x[9]==x[5]==x[1]==p2 and x[9]!="-" and x[5]!="-" and x[1]!="-"):
		p2_win=1
		print("Player2 win ...................! ")
		exit(0)
		

	elif(x[7]==x[5]==x[3]==p1 and x[7]!="-" and x[5]!="-" and x[3]!="-"):
		p1_win=1
		print("Player1 win ...................! ")
		exit(0)
		

	elif(x[7]==x[5]==x[3]==p2 and x[7]!="-" and x[5]!="-" and x[3]!="-"):
		p2_win=1
		print("Player2 win ...................! ")
		exit(0)
		

	elif(x[9]==x[8]==x[7]==p1 and x[9]!="-" and x[8]!="-" and x[7]!="-"):
		p1_win=1
		print("Player1 win ...................! ")
		exit(0)
		
	elif(x[9]==x[8]==x[7]==p2 and x[9]!="-" and x[8]!="-" and x[7]!="-"):
		p2_win=1
		print("Player2 win ...................! ")
		exit(0)
		

	elif(x[6]==x[5]==x[4]==p1 and x[6]!="-" and x[5]!="-" and x[4]!="-"):
		p1_win=1
		print("Player1 win ...................! ")
		exit(0)
		
	elif(x[6]==x[5]==x[4]==p2 and x[6]!="-" and x[5]!="-" and x[4]!="-"):
		p2_win=1
		print("Player2 win ...................! ")
		exit(0)
		

	elif(x[3]==x[2]==x[1]==p1 and x[3]!="-" and x[2]!="-" and x[1]!="-"):
		p1_win=1
		print("Player1 win ...................! ")
		exit(0)
		
	elif(x[3]==x[2]==x[1]==p2 and x[3]!="-" and x[2]!="-" and x[1]!="-"):
		p2_win=1
		print("Player2 win ...................! ")
		exit(0)
		

	elif(x[9]==x[6]==x[3]==p1 and x[9]!="-" and x[6]!="-" and x[3]!="-"):
		p1_win=1
		print("Player1 win ...................! ")
		exit(0)
	elif(x[9]==x[6]==x[3]==p2 and x[9]!="-" and x[6]!="-" and x[3]!="-"):
		p2_win=1
		print("Player2 win ...................! ")
		exit(0)
		

	elif(x[8]==x[5]==x[2]==p1 and x[8]!="-" and x[5]!="-" and x[2]!="-"):
		p1_win=1
		print("Player1 win ...................! ")
		exit(0)
		
	elif(x[8]==x[5]==x[2]==p2 and x[8]!="-" and x[5]!="-" and x[2]!="-"):
		p2_win=1
		print("Player2 win ...................! ")
		exit(0)

	elif(x[7]==x[4]==x[1]==p1 and x[7]!="-" and x[4]!="-" and x[1]!="-"):
		p1_win=1
		print("Player1 win ...................! ")
		exit(0)
		
	elif(x[7]==x[4]==x[1]==p2 and x[7]!="-" and x[4]!="-" and x[1]!="-"):
		p2_win=1
		print("Player2 win ...................! ")
		exit(0)
		


while 1:
		p1_play=input("Player1 : Enter your block [1-9]")
		switch(p1_play,1)
		p2_play=input("Player2 : Enter your block [1-9]")
		switch(p2_play,2)