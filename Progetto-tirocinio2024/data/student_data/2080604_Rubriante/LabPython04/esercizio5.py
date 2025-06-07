n=int(input("Inserisci un numero positivo: "))
fatt=n
if fatt==0:
    fatt=1
while n>1:
    fatt=fatt*(n-1)
    n-=1
print(fatt)
