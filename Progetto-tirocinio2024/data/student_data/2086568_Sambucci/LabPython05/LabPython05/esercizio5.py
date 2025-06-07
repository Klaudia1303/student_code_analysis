s=input('Inserire stringa: ')
while len(s)<2:
    print('Stringa troppo piccola!')
    s=input('Inserire stringa: ')

n=int(input('Inserire intero positivo: '))
while n<=0:
    print('Hai inserito un numero non positivo!')
    n=int(input('Inserire intero positivo: '))

corretto=False
i=0
while not corretto and i<len(s)-n:
    if s.count(s[i])>=2:
        if s[i]==s[i+n]:
            corretto=True
    i+=1
print(corretto)

