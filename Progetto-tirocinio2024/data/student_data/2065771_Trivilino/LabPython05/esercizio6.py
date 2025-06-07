s=input('Inserire una stringa: ')
risultato=0
for i in s:
    if s.count(i)>=2:
        distanza=s.rfind(i)-s.find(i)
        if distanza>risultato:
            risultato=distanza
print(risultato)
