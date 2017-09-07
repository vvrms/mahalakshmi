#!/user/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("press r to roll the dice:")                                                                                                                                                                                     
	if roll=="r":
		r=random.randint(1,6)	
		count=count+r
		print("your random num is",r)  
		print("you are on count",count)

	if count==8:
		count=37 
		print("you got a ladder",count)
	if count==13:
		count=34
		print("you got a ladder",count)
	if count==40:			
		count=6
		print("you got a ladder",count)	
	if count==52:			
		count=81
		print("you got a ladder",count)
	if count==76:				
		count=97
		print("you got a ladder",count)
	if count==11:			
		count=2	
		print("sinks down ",count)
	if count==25:
		count=4
		print("sinks down ",count)
	if count==38:			
		count=9	
		print("sinks down ",count)
	if count==65:			
		count=46	
		print("sinks down ",count)
	if count==89:				
		count=70
		print("sinks down ",count)
	if count==93:			
		count=64
		print("sinks down ",count)
print("congragulation you won")