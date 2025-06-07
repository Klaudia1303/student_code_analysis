"""Vesione col For"""
b=True; fattoriale=1
n=int(input("Inserire un numero per fare il fattoriale: "))
if n==0 or n==1:    print("\nFattoriale del numero inserito(For): ",fattoriale)
elif n>1:
    for i in range(n,1,-1):
        fattoriale*=i
    print("Fattoriale del numero inserito(For): ",fattoriale)

"""Versione col while"""

b=True; fattoriale=1
if n==0 or n==1:    print("\n\nFattoriale del numero inserito(While): ",fattoriale)
elif n>1:
    i=n
    while b:
        fattoriale*=i
        if i==1:    b=False
        i-=1
    print("Fattoriale del numero inserito(While): ",fattoriale)
