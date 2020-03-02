def f2c(fahr):
    celsius = 0.0
    celsius = (fahr - 32) * 5/9
    return round(celsius,2)

def test_f_90_2c():
    assert f2c(90) == 32.22

def test_f_986_2c():
    assert f2c(98.6) == 37.0

def test_f_100_2c():
    assert f2c(100) == 37.78

def test_f_32_2c():
    assert f2c(32) == 0.0

def test_f_212_2c():
    assert f2c(212) == 100

def test_f_50_2c():
    assert f2c(50) == 10.0

def test_f_100_2c():
    assert f2c(180) == 82.22

def test_f_1000_2c():
    assert f2c(2000) == 1093.33

def test_f_neg257_2c():
    assert f2c(-257) == -160.56

def test_f_0_2c():
    assert f2c(0) == -17.78