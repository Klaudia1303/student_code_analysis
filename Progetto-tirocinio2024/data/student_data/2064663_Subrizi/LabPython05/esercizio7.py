s=input('Inserisci una stringa: ')
corretto=False
for i in s:
    if s.count(i)>=2:
        corretto=True
print(corretto)
   
    
