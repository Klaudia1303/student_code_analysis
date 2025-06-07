s1 = input('Inserisci una prima stringa: ')
s2 = input('Inserisci una seconda stringa: ')
n = int(input('Inserisci un numero: '))
s=''
for i in range(len(s1)):
    f=s2.find(s1[i])
    if f==-1:
        continue
    
    if f-i<=n and i-f<=n:
        s=str(s)+str(s1[i])

print(s)



