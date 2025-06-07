n1=int(input("immetti primo intero: "))
n2=int(input("immetti secondo intero: "))
n3=int(input("immetti terzo intero: "))
if n1>=n2 and n1>=n3:
    primo=n1
    if n2>=n3:
        secondo=n2
        terzo=n3
    else:
        secondo=n3
        terzo=n2
elif n2>=n1 and n2>=n3:
    primo=n2
    if n1>=n3:
        secondo=n1
        terzo=n3
    else:
        secondo=n3
        terzo=n1
elif n3>=n1 and n3>=n2:
    primo=n3
    if n1>=n2:
        secondo=n1
        terzo=n2
    else:
        secondo=n2
        terzo=n1
print(primo)
print(secondo)
print(terzo)
