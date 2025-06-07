a=input('inserisci una stringa: ')
b=input('inserisci una stringa: ')
c=input('inserisci una stringa: ')
while len(a)+len(b)!=len(c):
    a=b
    b=c
    c=input('inserisci una stringa: ')
print(a,b,c)
    
