a=input('Inserisci una stringa: ')
b=input('Inserisci una seconda stringa: ')
c=input('Inserisci ancora una stringa: ')
while len(c)!=len(a)+len(b):
    a=b
    b=c
    c=input('Inserisci ancora una stringa: ')
print(a,b,c)
