s=input('inserire una stringa: ')
a=0
b=len(s)-1
valore=0
if s[:]==s[::-1]:
    print('la stringa è palindroma di livello:',len(s))    
else:
    while s[a]==s[b] and b!=0:
        a+=1
        b-=1
        valore+=1
    print('la stringa è palindroma di livello:',valore)
