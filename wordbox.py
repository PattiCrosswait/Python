word = input("Please enter a word: ")
#word = "MoXiE"
word = word.lower()

for count in range(len(word)):
    print(word)
    word = word[1:] + word[0]



