s=str(input('inserisci stringa palindroma:'))
while s[0::]!=s[::-1]:
    s=str(input('stringa non palindroma, inserire una stringa palindroma:'))
print('stringa palindroma di lunghezza:',len(s))    
