n=int(input("Inserire un numero intero maggiore di 0:  "))
p=0
g=1
s=1
if n<=0:
    print("Input non valido")
elif n==1:
    print(s)
else:
    while n>=p:
        print(s)
        s=p+g
        p=g
        g=s
        
