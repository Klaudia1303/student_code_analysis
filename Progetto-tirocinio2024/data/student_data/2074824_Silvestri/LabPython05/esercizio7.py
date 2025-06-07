s=input("Inserisci una stringa:")
finito=False
for i in s:
    x=s.count(i)
    if x>=2:
        finito=True
print(finito)
