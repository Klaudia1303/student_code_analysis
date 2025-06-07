n=int(input("Inserisci un intero maggiore o uguale a 0: "))
i=0
fatt=1
while i!=n:
    fatt *=(n-i)
    i +=1
print(fatt)
