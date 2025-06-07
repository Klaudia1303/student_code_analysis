word=input('insert word: ')
invWord=word[::-1]
palLevel=0
for counter in range(0,len(word)):
    if word[counter:counter+1]==invWord[counter:counter+1]:
        palLevel+=1
    elif word[counter:counter+1]!=invWord[counter:counter+1]:
        break

print(palLevel)