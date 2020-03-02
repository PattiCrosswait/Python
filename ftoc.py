def f2c(fahr):
    celsius = 0.0
    celsius = (fahr - 32) * 5/9
    return round(celsius,2)

def main():
    fahr = input("Enter a temperature in Fahrenhait: ")
    print(f2c(float(fahr)))

main()