#Scrivere un programma che legge in input 3 numeri interi, n1, n2, n3, e li stampa in ordine decrescente. Ad
#esempio, se n1=9, n2=14, n3=10, il programma deve stampare prima 14, poi 10 e successivamente 9, ossia
#“14
#10
#9”.

n1=int(input('inserisci il primo numero: '))
n2=int(input('inserisci il secondo numero: '))
n3=int(input('inserisci il terzo numero: '))
M= max(n1,n2,n3)
m= min(n1,n2,n3)

print (M)
if n1!=(M and m):
    print (n1)
elif n2!= (M and m):
        print(n2)
else:
    if n3!=(M and m):
        print(n3)
print(m)
