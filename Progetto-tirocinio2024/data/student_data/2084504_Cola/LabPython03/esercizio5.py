s=input('scrivere una frase: ')

while (s.islower()==False or s.isalpha()==False) and not len(s)==0:
    print(str(s[0])+str(s[-1]))
    s=input('scrivere una frase: ')



