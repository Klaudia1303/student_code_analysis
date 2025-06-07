s=input("inserire una stringa: ")
n=len(s)
x=0
y=0
while x<=n-1 and y<=100:
    y=int(ord(s[x]))
    x=x+1
    if x>n-1:
        print("stringa consumata e carattere non trovato")
    elif y>100:
        print("Il primo carattere con codice Unicode maggiore di 100 è",s[x-1])
