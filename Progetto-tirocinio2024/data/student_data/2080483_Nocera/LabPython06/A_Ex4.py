kmp1= int(input("inserire la velocità del primo viaggiatore :"))   
kmp2= int(input("inserire la velocità del secondo viaggiatore :"))    
giorno=0
vantaggio=kmp1+1
for i in range(1,1000):
    kmp1=kmp1+vantaggio
    arrivo=kmp2*i
    vantaggio+=1
    if kmp1>=arrivo:
        break
print(i)
