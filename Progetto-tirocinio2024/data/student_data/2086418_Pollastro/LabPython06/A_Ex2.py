s=str(input('inserisci stringa'))
l=len(s)
if l==1:print ('stringa palindroma di livello 1')
else:
    for i in range(0,len(s)):
        if s[i]!=s[l-i-1]:
            break
    if i==0: print ('parola non palindroma (livello 0)')
    elif s==s[::-1]: print('parola completamente palindroma (livello',l,')')
    else: print(s,'è palindroma di livello',i)
                   
