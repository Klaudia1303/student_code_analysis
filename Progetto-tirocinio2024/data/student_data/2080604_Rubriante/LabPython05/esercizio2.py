s=input("inserisci una stringa: ")
n=int(input("inserisci un numero: "))
ris=""
for i in range(len(s)):
    k=n
    while k>0:
        ris=ris+s[i]
        k-=1
print(ris)
