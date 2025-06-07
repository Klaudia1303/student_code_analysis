n=str(input("Inserire numero intero:"))
i=0
b=True
while b:
    if n.count("*")==1:
        b=False
        print(i)
        break
    elif n.count("-")==1:
        n=int(n)
        i=i
    else:
        n=int(n)
        i=i+1
        n=str(input("Inserire un altro numero intero:"))
    
