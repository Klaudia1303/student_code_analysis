m=input("inserisci una stringa:")
n=input("inerisci una nuova stringa:")
o=input("inserisci una nuova stringa:")
while len(n) + len(m)!=len(o):
    m=n
    n=o
    o=input("inserisci una nuova stringa:")
print(m,n,o)
