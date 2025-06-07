x=input('inserisci una stringa: ')
d=0
d1=0
for i in range(len(x)):
    if x.find(x[i])!= x.rfind (x[i]):
        d= x.rfind (x[i])- x.find(x[i])
        if d > d1:
            d1=d
print (d1)
