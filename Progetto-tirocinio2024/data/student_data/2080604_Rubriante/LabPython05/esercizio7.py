s=input("inserisci una stringa: ")
ris=False
for i in range(len(s)):
    if s.count(s[i])>1:
        ris=True
        break
    else:
        ris=False
print(ris)
