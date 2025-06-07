s=input('inserisci una stringa ')
while s!=''and s.islower()==False or s.isalpha()==False:
    print(s[0]+s[-1])
    s=input('inserisci una stringa ')
if s.islower()==True:
    print(s[0]+s[-1])
    
