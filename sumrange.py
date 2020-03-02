#Patti Crosswait
#sumrange.py


start = int(input('Enter the start integer: '))
stop = int(input('Enter the stop integer: '))

sumofSquares = 0
for counter in range(start, stop+1, 1):
   print(counter)
   counterSquared = counter ** 2
   print(counterSquared)
   sumofSquares = sumofSquares + counter ** 2

print(sumofSquares)