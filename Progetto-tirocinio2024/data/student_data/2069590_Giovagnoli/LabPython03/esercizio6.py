s = input("Inserire una stringa non vuota: ")
if s!="":
    i=0
    while i<len(s):
        print(ord(s[i]))
        if ord(s[i])>100:
            print("Il carattere: ",s[i]," ha codice Unicode maggiore di 100!")
            break
        else:
            i+=1
        if i==len(s):
            print("stringa consumata e carattere non trovato")