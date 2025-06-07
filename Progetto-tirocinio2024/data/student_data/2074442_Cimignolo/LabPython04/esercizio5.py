n=int(input('inserisci un numero positivo: '))

if n==0:
    print(1)
else:
    u=1
    fatt=1
    while n>=u:
        fatt=fatt*u
        u+=1
    print(fatt)
