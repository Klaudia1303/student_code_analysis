s = input ('Inserisci una stringa di testo: ')
lvl = 0
for i in range (len(s)//2):
    if s[i] == s[len(s)-1-i]:
        lvl = lvl + 1
    else :
        break
if lvl >= len(s)/2:
    print ('livello',len(s))
else :
    print ('livello',lvl)
