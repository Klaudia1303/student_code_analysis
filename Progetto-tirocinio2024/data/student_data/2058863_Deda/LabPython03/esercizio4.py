x=int(input('Inserisci un intero compreso da 0 a 10 '))
y=int(input('Inserisci un intero compreso da 0 a 10 '))
i=0
while 0<=x<=10 and 0<=y<=10 and 0<=i<=10:
    if i!=x and i!=y:
        print(i)
        i +=1
    else:
        i +=1
