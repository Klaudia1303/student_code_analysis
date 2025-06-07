x=input("inserisci un intero ")
k=0
while x!='0':
    if int(x) %3 ==0: 
        k=k+int(x)
    x=input("inserisci un intero ")
print (k)