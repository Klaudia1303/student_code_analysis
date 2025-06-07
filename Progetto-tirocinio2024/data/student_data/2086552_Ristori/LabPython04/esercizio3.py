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
        i=i+n
    else:
        n=int(n)
        i=i
    n=str(input("Inserire un altro numero intero:"))
    
