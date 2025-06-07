v1=int(input('inserisci la velocotà del primo viaggiatore:'))
v2=int(input('inserisci la velocotà del secondo viaggiatore:'))
tot=0
e=1
for i in range(1,1001):
    v1+=20
    v2+=e
    e+=1
    tot+=1
    if v2>=v1:
        print(tot)
        break
