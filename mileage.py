#Patti Crosswait
#mileage.py

#Write a program that will compute MPG for a car.
#Prompt the user to enter the number of miles driven and the number of gallons used.
#Print a nice message with the answer.

miles = float(input('Enter the number of miles driven: '))
gallons = float(input('Enter the number of gallons used: '))

MPG  = miles/gallons
print('MPG: ' + str(MPG) + ' miles/gallom')