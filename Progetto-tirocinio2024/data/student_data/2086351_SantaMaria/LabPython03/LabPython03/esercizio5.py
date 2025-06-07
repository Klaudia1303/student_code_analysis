i=0
s=input('Inserisci una stringa: ')
while i>=0:
    if s.isalpha()==False or s.islower()==False:
        print(s[0]+s[len(s)-1])
        s=input('Inserisci una stringa: ')
        i+=1
    else:
        i=-1
        print(s[0]+s[len(s)-1])
