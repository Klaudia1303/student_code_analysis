n = str(input("scrivere una parola :"))
i = 0
while i<(len(n)):
    unicode = ord(n[i])
    i+=1
    if unicode >100:
        print("il primo carattere con codice Unicode maggiore di 100 è ",chr(unicode))
        i= i+len(n)
    elif i==len(n):
        print("stringa consumata e carattere non trovato")


