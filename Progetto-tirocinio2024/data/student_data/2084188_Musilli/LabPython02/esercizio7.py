print("ESERCIZIO 7: dati 3 numeri interi, si stampino in ordine decrescente\n")
n1=int(input("Inserire il primo numero: \t"))
n2=int(input("Inserire il secondo numero: \t"))
n3=int(input("Inserire il terzo numero: \t"))
if n1!=n2 and n2!=n3 and n1!=n3:
    print("\n\t\tStampa in ordine decrescente:")
    if n1>n2 and n1>n3:
        print("\n\t\t",n1,"\n\t\t",n2,"\n\t\t",n3)
    elif n1>n2 and n1<n3:
        print("\n\t\t",n3,"\n\t\t",n2,"\n\t\t",n1)
    elif n2>n1 and n2>n3:
        print("\n\t\t",n2,"\n\t\t",n3,"\n\t\t",n1)
    elif n2>n1 and n2<n3:
        print("\n\t\t",n3,"\n\t\t",n2,"\n\t\t",n1)
else:
    print("I numeri inseriti sono uguali")

#versione snella-veloce
#num=[n1,n2,n3]
#num.sort(reverse=True)
#print(num)
