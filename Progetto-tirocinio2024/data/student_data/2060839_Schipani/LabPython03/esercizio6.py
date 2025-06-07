s=input('inserisci una stringa ')
i=0
while i<len(s) and ord(s[i])<100:
        print(s[i])
        i+=1
if i==len(s):
        print('stringa consumata carattere non trovato')
elif ord(s[i])>=100:
         print('il primo carattere con codie Unicode maggiore di 100 è ',s[i])
