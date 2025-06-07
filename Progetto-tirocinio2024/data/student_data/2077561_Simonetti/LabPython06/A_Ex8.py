s1=input('Please enter a word: ')
s2=input('Please enter a second word: ')
n=int(input('Please enter a number: '))
final=''
for i in range(len(s1)):
    if s1[i] in s2:
        position=s1.find(s1[i])
        if s1[i] in s2[position-n:position] or s1[i] in s2[position:position+n+1]:
            final+=s1[i]
print(final)
