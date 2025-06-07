s=input("scrivi una parola di almeno due caratteri :")
n=int(input("inserisci un numero per la distanza :"))
if len(s)>=2:
    entrato=False
    for i in range(len(s)):
        car1=s[i]
        if i+n<len(s) and s[i]==s[i+n]:
            entrato=True
    print(entrato)
        
        
else:
    print("la stringa è troppo piccola")
    
