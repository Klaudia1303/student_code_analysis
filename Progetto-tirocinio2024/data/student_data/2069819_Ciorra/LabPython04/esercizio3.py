x=input("inserisci un intero ")
k=0
while x!='*':
    if int(x) < 0 : 
        k=k+int(x)
    x=input("inserisci un intero ")
print (k)