s=input('inserisci una stringa: ')
r=input('inserisci una stringa della stessa lunghezza: ')
i=0
if len(s)==len(r):
   for i in range(len(s)):
       print(s[i]+r[i],end='')

