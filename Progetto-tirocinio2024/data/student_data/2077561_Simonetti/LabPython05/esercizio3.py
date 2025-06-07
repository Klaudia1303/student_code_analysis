s1=input('please enter a word: ')
s2=input('please enter a word: ')
newS=''
for i in s1:
    if i not in s2:
        newS+=i
print(newS)
