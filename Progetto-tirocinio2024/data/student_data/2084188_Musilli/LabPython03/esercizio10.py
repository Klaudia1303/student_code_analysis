b=True
while b:
    n=int(input("Inserire un numero per stampare \
 tutti i numeri primi da 2 fino al numero inserito: "))
    if not n>1: print("Si prega di reinserire. Il numero non è maggiore di 1\n")
    else: b=False
i=2
while i<=n:
    b=True;c=1;p=0
    while b:
        if i%c==0:  p+=1
        c+=1
        if c>i: b=False
    if p<3: print("\n",i)
    i+=1
