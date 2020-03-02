def reverse(st):
    reversed = ''
    for char in st:
        reversed = char + reversed
    return reversed


def main():
    starting = input("Enter a string: ")
    print(reverse(starting))


main()