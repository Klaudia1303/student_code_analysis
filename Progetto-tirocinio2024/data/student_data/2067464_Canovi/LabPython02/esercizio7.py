n1 = input("inserisci un numero intero: ")
n1 = int(n1)
n2 = input("inserisci un numero intero: ")
n2 = int(n2)
n3 = input("inserisci un numero intero: ")
n3 = int(n3)

if n1 == max(n1,n2,n3):
    if n2<=n3:
        print(n1,n3,n2)
    else:   print(n1,n2,n3)

elif n2 == max(n1,n2,n3):
    if n1<=n3:
        print(n2,n3,n1)
    else:   print(n2,n1,n3)

elif n3 == max(n1,n2,n3):
    if n1<=n2:
        print(n3,n2,n1)
    else:   print(n3,n1,n2)
    

