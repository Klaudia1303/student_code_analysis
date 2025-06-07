word=input('insert word: ')
newTopCount=0
topCount=0
topLetter=''
for letter in word:
    for counter in range(len(word)):
        if letter==word[counter:counter+1]:
            newTopLetter=letter
            newTopCount+=1
    if newTopCount>=topCount:
        topCount=newTopCount
        topLetter=newTopLetter
    newTopCount=0
    newTopLetter=''
print(topLetter,topCount)