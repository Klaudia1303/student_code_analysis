x=int(input('inserisci un intero compreso fra 0 e 10: '))
y=int(input('inserisci un altro intero compreso fra 0 e 10: '))
i=0
while i<=10:
    if i==x or i==y:
        i=i+1
    else:
        print(str(i))
        i=i+1
