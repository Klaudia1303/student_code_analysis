
a=input("Inserisci stringa palindroma:\t")

b=a[::-1]

while b!=a:
    a=input("Inserisci davvero una stringa palindroma:\t")
    b=a[::-1]
print("stringa palindroma di lunghezza",len(a))
