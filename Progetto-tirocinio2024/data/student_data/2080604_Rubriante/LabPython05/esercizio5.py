s=input("inserisci una stringa: ")
n=int(input("inserisci un numero: "))
ris=False
for i in range(len(s)):
    if i+n<len(s):
        if s[i]==s[i+n]:
            ris=True
            break
        else:
            ris=False
    else:
        ris=False
print(ris)
        
