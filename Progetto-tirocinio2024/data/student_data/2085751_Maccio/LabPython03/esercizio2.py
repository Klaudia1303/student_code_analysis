n=int(input("Inserire un numero maggiore di 0:  "))
if n>0:
    i=1
    while n>i:
        if n%i==0:
            print("Un divisore di",n,"è",i)
            i=i+1
        else:
            i=i+1
else:
    print("Input non valido")
    
