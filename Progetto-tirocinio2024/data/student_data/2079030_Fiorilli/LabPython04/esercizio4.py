n=input('inserisci un valore intero: ')
s=0
while int(n)!=0:
    if int(n)%3==0:
        s=s+int(n)
    n=input('inserisci un valore intero: ')
print (s) 
