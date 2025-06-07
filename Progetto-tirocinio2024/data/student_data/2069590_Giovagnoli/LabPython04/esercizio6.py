n=int(input("Inserire il primo numero intero: "))
n1=int(input("Inserire il secondo numero intero: "))
print("I due numeri verranno moltiplicati!")
prodotto=0
while n1!=0:
    if n1>0:
        prodotto = prodotto+n
        n1-=1
    else:
        prodotto = prodotto-n
        n1+=1
print("Il prodotto è: ",prodotto)