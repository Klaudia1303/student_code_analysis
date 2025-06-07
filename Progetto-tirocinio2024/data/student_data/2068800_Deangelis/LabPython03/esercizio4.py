n=-1
m=11
while n<0 and m>10:
    n = int((input("Inserisci un numero intero maggiore di 0: ")))
    m = int((input("Inserisci un numero intero minore di 11: ")))

i=0
while i<=10:
    if i!=n and i!=m:
        print(i)
    i=i+1
