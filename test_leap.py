def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    

def test_leap_2000():
    assert is_leap(2000) == True
    
def test_leap_1973():
    assert is_leap(1973) == False
    
def test_leap_2016():
    assert is_leap(2016) == True
    
def test_leap_1991():
    assert is_leap(1991) == False
    
def test_leap_1995():
    assert is_leap(1995) == False
    
def test_leap_1939():
    assert is_leap(1939) == False
    
def test_leap_1940():
    assert is_leap(1940) == True
    
def test_leap_2020():
    assert is_leap(2020) == True
    
def test_leap_2023():
    assert is_leap(2023) == False
    
def test_leap_1998():
    assert is_leap(1998) == False
