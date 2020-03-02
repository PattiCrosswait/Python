def triangle(N):
    for count in range(N):
        #for num in range(count):
        #    print('B',end='')
            #print('count:' + str(count)) + 'print 4-count '*''
        print('*',end='')
        #print()
    
def hollow_box(N):
    for count in range(N):
        print('*',end='')
    print()
    
    for count in range(N-2):
        print('*',end='')    
        for count in range(N-2):
            print(' ',end='')
        print('*',end='')
        print()
    #print()
    
    for count in range(N):
        print('*',end='')
        

N = int(input("Please enter an integer greater or equal to 0: "))
triangle(N)
hollow_box(N)