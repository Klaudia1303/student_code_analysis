x=input("Inserire una stringa di almeno 1 carattere: ")
lun=len(x)
n=0
while lun>n:
    if ord(x[n])>100:
        print("il primo carattere  con codice Unicode maggiore di 100 è \""+x[n]+"\" ")
        break
    n+=1
if n==lun:
    print("stringa consumata e carattere non trovato")
