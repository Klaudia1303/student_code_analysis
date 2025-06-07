n1=int(input("Inserire il primo numero da moltiplicare: "))
n2=int(input("Inserire il secondo numero per moltiplicare il primo: "))
prodotto=0
if n1<0 and n2<0: n1=-n1; n2=-n2
if n2<0 and n1>0: n2=-n2; n1=-n1

for i in range(n2):
    prodotto+=n1
print("Prodotto:",prodotto)
