s='b'
s_lette=0

while s.find('c')==-1 and s.find('a')==-1:
    s=input('Inserisci una stringa (contenente "a" e "c" per terminare): ')
    s_lette+=1
print(s_lette)
