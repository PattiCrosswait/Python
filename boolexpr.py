def is_in_semester(month,day):
    '''Write a Boolean (bool) function is_in_semester(month,day) that returns 
    #True when month/day falls within the dates of our current GPS Fall Semester 2019, 
    #starting on September 4 and ending on December 13. If month/day falls outside this range 
    #(which includes both starting and ending dates), return False.'''

    if month < 9:
        return False
    elif month == 9:
        if day < 4:
            return False
        else:
            return True
    elif month == 12:
        if day > 13:
            return False
        else:
            return True
    elif month == 10 or month == 11:
        return True
        
    
def main():
    '''function that reads integers month and day from the user, 
    calls is_in_semester(month,day), 
    then prints out 'month/day is in Fall Semester' or 'month/day is NOT in Fall Semester'. 
    Example for month==12, day==1 => print 12/1 is in Fall Semester. Finally, call main() as the last statement in your .py file.
    ​en write a main() function that reads integers month and day from the user, 
    calls is_in_semester(month,day), 
    Note that your function should only return True or False, with main()calling is_in_semester(...), 
    then printing out the text which depends upon its bool returned value.'''

    month = int(input('Enter a number between 1-12: '))
    day = int(input('Enter a number between 1-31: '))
    result = is_in_semester(month,day)
    
    if result:
        print('month/day is in Fall Semester') #return true
    else:
        print('month/day is NOT in Fall Semester') #return true
        #return false
    
main()


