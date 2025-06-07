n = int(input("inserisci numero: "))
i=2
j=0
while i<n:
    if n%i==0:
        j+=1
    i+=1
if j>0:
     print("numero non primo")
else:
     print("numro primo")
