#v1=20km x giorno
#v2=km x giorno = num giorno
v1=0
v2=0
for i in range (1,1000):
    v1+=20
    v2+=i
    if v1==v2:
        print(i)
        break
