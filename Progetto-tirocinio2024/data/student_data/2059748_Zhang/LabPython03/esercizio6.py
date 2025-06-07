s=input("scrivi una parola: ")
x=0
while x<len(s) and ord(s[x])<100:
     x+=1
if x==len(s):
    print("stringa consumata e carattere non trovato")
else:
    print("Il primo carattere con codice Unicode maggiore di 100 è: " +s[x])
