s=input('inserisci una stringa (a e c per terminare): ')
i=0
while 'c' not in s or 'a' not in s:
    s=input('inserisci una stringa (a e c per terminare): ')
    i=i+1
print(i+1)
