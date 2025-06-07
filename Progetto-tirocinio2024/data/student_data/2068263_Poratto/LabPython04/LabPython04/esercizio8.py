b=str(input('inserisci una stringa: '))
c=str(input('inserisci una stringa: '))
while b[len(b)-1]!=c[0]:
    b=c
    c=str(input('inserisci una stringa: '))
print(b,c)
