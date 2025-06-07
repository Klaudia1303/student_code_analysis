s=input('inserisci una stringa: ')

ris=False

for c in s:
    if s.count(c)>1:
        ris=True
print(ris)
