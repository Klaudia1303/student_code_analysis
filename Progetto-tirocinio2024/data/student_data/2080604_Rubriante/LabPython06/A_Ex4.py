v1=int(input("Inserisci la prima velocità: "))
v2=int(input("Inserisci la seconda velocità: "))
d1=0
d2=0
for i in range(1,1000):
    d1=d1+v1
    d2=d2+(v2*i)
    if d1<=d2:
        break
print(i)
