s=input('Inserisci una stringa di almeno 2 caratteri ')
d=False
for i in range(len(s)):
    if (s.count(s[i])>=2):
        doppio=s[i]
        d=True
        mass=1
        dist=s.rfind(doppio)-s.find(doppio)
        if dist>mass:
            mass=dist
if d==False:
    print('0')
else:
    print(mass)
