n1 = int(input("Inserisci un numero intero: "))
n2 = int(input("Inserisci un numero intero: "))
if n1 >0 and n2 >0:
    a = min(n1,n2)
    b = max(n1,n2)
for i in range (a,b,a):
    print(i)
