s=input('inserisci una stringa' )
c=0
for i in range(len(s)):
    if s[i]==s[len(s)-(i+1)]:
        c+=1
    else:
        break
if c>0:
    print('la stringa è palindroma di livello',c)
else:
    print('la stringa non è palindroma')
