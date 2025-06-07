s=input("inserire stringa:")
cont=1
car=s[0]
frqCar=[s[0],1]
for i in range (1,len(s)):
    if car==s[i]:
        cont+=1
        if frqCar[1]<cont:
            frqCar[1]=cont
        if frqCar[0]!=car:
            frqCar[0]=car
    else:
        cont=0
        car=s[i]
print(frqCar[0],frqCar[1])
