s1= input('stringa1: ')
s2= input('stringa2: ')
x=0
par= ''
for i in range(len(s1)):
    volte=s2.count(s1[x])
    if volte < 1:
        par = par + s1[x]
    x= x+1
print(par)
