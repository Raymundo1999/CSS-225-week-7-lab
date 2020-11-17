#Raymundo Sanchez
#Nov 16, 2020
#this code will give a random integer in between 25 and 35
#the count makes it so after a number it adds a 1 to go to the next number
import random
count = 0
while count < 10:
    print ("Random integer: ", random.randint(25,35))
#the count = count + 1 adds a 1 to the count example: 0+1=1, 1+1=2 ,2+1=3
    count += 1
