#Scrivere un programma che legge in input 3 numeri interi, n1, n2, n3,
#e li stampa in ordine decrescente. Ad esempio, se n1=9, n2=14, n3=10,
#il programma deve stampare prima 14, poi 10 e successivamente 9, ossia
#“14 10 9”.
n1=int(input("Inerisci il primo numero:"))
n2=int(input("Inerisci il secondo numero:"))
n3=int(input("Inerisci il terzo numero:"))
if (n1>n2>n3):
    print(n1, n2, n3)
elif (n2>n1>n3):
    print(n2, n1, n3)
elif (n3>n1>n2):
    print(n3, n1, n2)
elif (n1>n3>n2):
    print(n1, n3, n2)
elif (n2>n3>n1):
    print(n2, n3, n1)
elif (n3>n2>n1):
    print(n3, n2, n1)
