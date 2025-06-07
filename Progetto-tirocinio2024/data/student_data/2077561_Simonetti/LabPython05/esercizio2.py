s=input('please enter a word or phrase (you can use whitespace): ')
n=int(input('please enter a number greater than 0: '))
newS=''
if n>0:
    for i in range(len(s)):
        if s[i]==' ':
            newS+=s[i]
        else:
            newS+=s[i]*n
    print(newS)
else:
    print('end.')
