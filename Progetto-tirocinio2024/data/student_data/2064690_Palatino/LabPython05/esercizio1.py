s=input('inserisci una stringa: ')
t=input('inserisci una stringa della stessa lunghezza di s: ')
for i in range(len(s)):
    k=s[i]+t[i]
    print(k,end='')
