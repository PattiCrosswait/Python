def speeding_fine(speed_limit,current_speed):
    base_fine = 50
    mileage_fine = (5 * (current_speed - speed_limit))
    fine = base_fine + mileage_fine
    
    if current_speed > 90:
        fine = fine + 200
    
    return fine
        
def main():
    
    speed_limit = float(input('Enter the speed limit:'))
    current_speed = float(input('Enter the current speed:'))
    
    if current_speed - speed_limit <= 0:
        print('The speed is legal.')
    else:
        fine = speeding_fine(speed_limit,current_speed)
        print('The speed is illegal.  The fine is: ' + str(fine))
    
main()