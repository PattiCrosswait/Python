#1.0 + 2.0 * 2 ** 3 ** 2 % 3 - 6 // 4
#(1.0 + ((2.0 * (2 ** (3 ** 2))) % 3) - (6 // 4))

expr1 = 3 ** 2
expr2 = 2 ** expr1

expr3 = 2.0 * expr2
expr4 = expr3 % 3
expr5 = 6 // 4
expr6 = expr4 - expr5

result = 1.0 + expr6
print(result)
print(1.0 + 2.0 * 2 ** 3 ** 2 % 3 - 6 // 4)
