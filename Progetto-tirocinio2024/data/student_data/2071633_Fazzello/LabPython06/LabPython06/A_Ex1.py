##1. Scrivere un programma Python che prende in input due numeri interi n1 e n2 maggiori di 0 e stampa in
##ordine decrescente tutti i divisori di n1 che NON sono divisori di n2. Ad esempio, se n1 vale 24 e n2 vale 6
##allora deve stampare (uno per riga): 24, 12, 8, 4.

n1=int(input('inserire un numero maggiore di zero: '))
n2=int(input('inserire un numero maggiore di zero: '))
x=0
for i in range(n1):
    if n2%(n1-x)!=0 and n1%(n1-x)==0:
        print(n1-x)
    x=x+1
