
n=int(input("Inserire numero intero:"))
b=True
i=0
while b:
    if n%3==0:
        i=i+n
    if n==0:
        b=False
        print(i)
    else:
        n=int(input("Inserire un altro numero intero:"))
    
