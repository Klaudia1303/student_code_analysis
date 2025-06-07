s=str(input('please type a word: '))
if len(s)==0:
    print('Error: the string is empty.')
elif len(s)==1:
    print('string is too short.')
elif s[0]==s[len(s)-1]:
    print('caratteri iniziale e finale uguali')
