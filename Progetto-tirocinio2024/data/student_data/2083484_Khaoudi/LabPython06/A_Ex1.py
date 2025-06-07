#Scrivere un programma Python che prende in input due numeri interi n1 e n2 maggiori di 0 e stampa in
#ordine decrescente tutti i divisori di n1 che NON sono divisori di n2. Ad esempio, se n1 vale 24 e n2 vale 6
#allora deve stampare (uno per riga): 24, 12, 8, 4.
n1=int(input("Inserisci un numero intero :  "))
n2=int(input("Inserisci un numero intero :  "))
i=n1
while i>0:
    if(n2%i!=0):
        if n1%i==0:
            print(i)
    i-=1

