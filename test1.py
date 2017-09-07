#!/user/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("press r to roll the dice: ")                                                                                                                                                                                     
	elif roll=="r":
		r=random.randint(1,6)	
		count=count+r
		  print ("your random num is",r)  
		  print ("you are on count",count)
		
	elif count==8:
		 count=37 
		     print ("you got a ladder",count)
	elif count==13:
		 count=34
		     print ("you got a ladder",count)
	elif count==40:			
		 count=6
		     print ("you got a ladder",count)
	
						
	elif count==52:			
		 count=81
		     print ("you got a ladder",count)
	elif count==76:				
		 count=97
		     print ("you got a ladder",count)
	elif count==11:			
		 count=2	
		     print ("sinks down ",count)
	elif count==25:
		 count=4
		     print ("sinks down ",count)
	elif count==38:			
		 count=9	
		     print ("sinks down ",count)
	elif count==65:			
		 count=46	
		     print ("sinks down ",count)
	elif count==89:				
		 count=70
		     print ("sinks down ",count)
	elif count==93:			
		 count=64
		     print ("sinks down ",count)
		 