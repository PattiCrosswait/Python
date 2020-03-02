#Write a Python program that reads the taxable income income as a float value from the user, 
#then calculate and print out the tax for an unmarried individual with that taxable income. 
#Use the table to the right...
#You should also check that the entered income is >= 0.0; otherwise print "Bad input" and quit.

def income_tax(income):
    if income > 0 and income <= 9700:
        tax = income * .10
    elif income > 9700 and income <= 39475:
        tax = income * .12
    elif income > 39475 and income <= 84200:
        tax = income * .22
    elif income > 84200 and income <= 160725:
        tax = income * .24
    elif income > 160725 and income <= 204100:
        tax = income * .32
    elif income > 204100 and income <= 510300:
        tax = income * .35
    elif income > 510300:
        tax = income * .37
    return tax
        
def main():
    income = float(input('Enter the income of an unmarried individual: '))
    
    if income < 0.0:
        print('Bad Input')
    else:
        tax = income_tax(income)
        print('The tax on that income for an unmarried individual is: ' + str(tax))
   
main()