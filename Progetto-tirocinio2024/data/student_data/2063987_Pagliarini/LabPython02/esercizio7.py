n1=int(input("inserisci un numero"))
n2=int(input("inserisci un numero"))
n3=int(input("inserisci un numero"))

if (n1<=n2):
    if (n2<=n3):
        print(n3 , n2 , n1)
    elif (n3>=n1):
        print(n2 , n3 , n1)
    else :
        print(n2 , n1 , n3)
elif (n2<=n1):
    if (n1<=n3):
        print(n3 , n1 , n2)
    elif (n2<=n3):
        print(n1 , n3 , n2)
    else :
        print(n1 , n2 , n3)
