word1=input('insert word: ')
word2=input('insert word: ')
finalLetters=''
repeated=False

for lettersW1 in word1:
    for lettersW2 in word2:
        if lettersW1==lettersW2:
            repeated=True
    if not repeated:
        finalLetters+=lettersW1
    repeated=False
print(finalLetters)