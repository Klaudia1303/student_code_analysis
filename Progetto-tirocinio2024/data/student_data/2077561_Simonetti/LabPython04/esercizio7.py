s=input('please type a word: ')
zeroTest=0
s=s[::-1]
i=0
character=''
while i<len(s):
    character=s[i]
    count=s.count(character)
    if count>zeroTest:
        zeroTest=count
        maxChar=character
    i+=1

print(maxChar)
