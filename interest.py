#Patti Crosswait
#interest.py

'''The formula for computing the final amount if one is earning compound
interest is given on Wikipedia as

A = P (1 + r/n)**nt

formula for compound interest
Write a Python program that assigns the principal amount of 10000 to variable P,
assign to n the value 12, and assign to r the interest rate of 8% (0.08).
Then have the program prompt the user for the number of years, t, that the money
will be compounded for.
Calculate and print the final amount after t years.'''

Principal = 10000
n = 12
rate = 0.08
time_years = float(input('Enter the number of years to compound interest: '))
exponent = n * time_years

Amount = Principal * ((1 + rate/n) ** exponent)
print('The amount after t years is: ' + str(Amount))