n1 = input("Inserisci il primo numero intero: ")
n1 = int (n1)
n2 = input("Inserisci il secondo numero intero: ")
n2 = int(n2)
n3 = input("Inserisci il terzo numero intero: ")
n3 = int(n3)
if n1 > n2 and n2 > n3:
    print(n1, n2, n3)
else:
    if n1 > n2 and n3> n2 and n1 > n3:
        print(n1, n3, n2)
    else:
        if n2 > n1 and n1 > n3:
            print(n2, n1, n3)
        else:
            if n2 > n1 and n3 > n1 and n2> n3:
                print(n2, n3, n1)
            else:
                if n3 > n1 and n1 > n2:
                    print(n3, n1, n2)
                else:
                    print(n3, n2, n1)
