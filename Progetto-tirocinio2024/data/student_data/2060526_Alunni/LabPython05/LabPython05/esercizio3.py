x=(input('inserisci una stringa:  '))
y=(input('inserisci una stringa:  '))
s=str()
l=0
for i in (x):
    if i not in y:
        s=(s+i)
        l+=1
print(s)
