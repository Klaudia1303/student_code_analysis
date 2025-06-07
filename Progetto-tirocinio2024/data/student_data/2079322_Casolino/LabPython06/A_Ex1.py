#Scrivere un programma Python che prende in input due numeri interi n1 e n2
#maggiori di 0 e stampa in ordine decrescente tutti i divisori di n1 che NON
#sono divisori di n2.
#Ad esempio, se n1 vale 24 e n2 vale 6 allora deve stampare (uno per riga):
#24, 12, 8, 4.

n1 = int(input("Inserire un primo numero intero: "))
n2 = int(input("Inserire un secondo numero intero: "))
count=n1
while count>0:
    if n1%count==0 and n2%count!=0:
        print(count)
        count-=1
    else:
        count-=1
        
            
