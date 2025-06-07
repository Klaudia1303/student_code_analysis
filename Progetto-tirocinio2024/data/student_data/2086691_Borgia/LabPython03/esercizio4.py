x=int(input("Inserire un numero intero compreso tra 0 e 10"))
y=int(input("Inserire un numero intero compreso tra 0 e 10"))
if x<0 or x>10 or y<0 or y>10:
    print("Numero non valido")
s=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while s<10:
    if s[i]==x or s[i]==y:
        s.replace(s[i],'')
    
