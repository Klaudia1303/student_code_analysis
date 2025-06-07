word=input('insert word: ')
number=int(input('insert a number: '))
repeat=False
for letterPos in range(0,len(word)):
    if word[letterPos:letterPos+1]==word[letterPos+number:letterPos+1+number]:
        repeat=True
print(repeat)