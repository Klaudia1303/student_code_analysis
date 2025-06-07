word=input('insert word: ')
oldMax=0
letterMax=''
letterCounter=0
for letter in word:
    for count in range(0,len(word)):
        if letter==word[count:count+1]:
            letterCounter+=1
        if oldMax<=letterCounter:
            oldMax=letterCounter
            letterMax=letter
    letterCounter=0
print(letterMax)