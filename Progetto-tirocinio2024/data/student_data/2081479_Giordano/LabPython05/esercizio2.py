word=input('insert word: ')
repeat=int(input('insert a number: '))
repeated=''
for counter in range(0,len(word)):
    repeated+=((word[counter:counter+1])*repeat)
print(repeated)