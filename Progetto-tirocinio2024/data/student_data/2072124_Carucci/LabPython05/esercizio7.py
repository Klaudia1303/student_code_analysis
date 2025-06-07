s = input('Inserire una stringa: ')

trovato = False
i = 0
while (not trovato) and i<len(s):
    if s.count(s[i])>1:
        trovato = True
    i+=1
print('Almeno un carattere compare più di una volta :', trovato) 
