s=input("Inserire una stringa: ")
i=0
while ord(s[i])>101 or i>len(s):
    print(s[i])
    i+=1
if ord(s[i])>101:
        print("Il primo carattere con codice Unicode maggiore di 100 è",s[i])
elif i>len(s):
        print("stringa consumata e carattere non trovato")
