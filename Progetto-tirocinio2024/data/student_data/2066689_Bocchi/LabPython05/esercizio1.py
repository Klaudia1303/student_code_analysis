s1= input('stringa1: ')
s2= input('stringa2: ')
x=0
par= ''
for i in range(len(s1)):
    par= par + s1[x] + s2[x]
    x+=1
print(par)
