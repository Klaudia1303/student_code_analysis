
c=input("Inserisci carattere:\t")

a=input("Inserisci stringa:\t")
n=a.count(c)

while n<=2:
    a=input("Inserisci stringa:\t")
    n=a.count(c)
print(n)
