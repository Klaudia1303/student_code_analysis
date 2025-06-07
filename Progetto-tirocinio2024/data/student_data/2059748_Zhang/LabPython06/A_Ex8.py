s1=str(input("scrivi una stringa: "))
s2=str(input("scrivi una stringa: "))
n=int(input("scrivi un numero: "))
x=''

for i in range(len(s1)):
    c=s1[i]
    for pos,car in enumerate(s2):
        if(car==c):
            if (s1.find(car))-(s2.find(c))<=n:
                x+=s1[i]
print(x)
