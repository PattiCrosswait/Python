def reverse(st):
    reversed = ''
    for char in st:
        reversed = char + reversed
    return reversed

def test_reverse1():
    assert reverse('tamara') == 'aramat'

def test_reverse2():
    assert reverse('patti') == 'ittap'

def test_reverse3():
    assert reverse('eric') == 'cire'

def test_reverse4():
    assert reverse('maxine') == 'enixam'

def test_reverse5():
    assert reverse('ruth') == 'htur'

def test_reverse6():
    assert reverse('geraldine') == 'enidlareg'

def test_reverse7():
    assert reverse('susan') == 'nasus'

def test_reverse8():
    assert reverse('tammi') == 'immat'

def test_reverse9():
    assert reverse('james') == 'semaj'

def test_reverse10():
    assert reverse('crosswait') == 'tiawssorc'