s=input('Inserisci una stringa: ')
r=input('Inserisci una seconda stringa: ')
u=s
while s[-1]!=r[0]:
        s=r[-1]
        u=r
        r=input('Inserisci ancora una stringa: ')
print(u,r)
