s=input("inserire una stringa")
a="b"
n=0
while ord(a)<100:
     a=s[n:n+1]
     n=n+1
     if a!="":
         if ord(a)>=100:
             print("Il primo carattere con codice Unicode maggiore di 100 è",a)
     else :
         a="z"
         print("stringa consumata e carattere non trovato")

     
     
    
