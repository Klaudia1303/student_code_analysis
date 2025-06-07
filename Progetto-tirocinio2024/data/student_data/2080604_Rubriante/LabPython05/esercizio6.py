s=input("inserisci una stringa: ")
ris=0
for i in range(len(s)):
    if ris<s.rfind(s[i])-s.find(s[i]):
        ris=s.rfind(s[i])-s.find(s[i])
print(ris)
        
