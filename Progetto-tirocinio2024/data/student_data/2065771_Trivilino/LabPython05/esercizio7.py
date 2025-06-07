s=input('Inserire una stringa: ')
risultato=False
for i in s:
    if s.count(i)>=2:
        risultato=True
        break
print(risultato)
