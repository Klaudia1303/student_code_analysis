s='ab'
while not str(s)==str(s)[::-1]:
 s=input('inserisci una stringa palindroma ')
 if not str(s)==str(s)[::-1]:
     print('stringa non palindroma, inserire una stringa palindroma')
print('stringa palindroma di lunghezza',len(s))
