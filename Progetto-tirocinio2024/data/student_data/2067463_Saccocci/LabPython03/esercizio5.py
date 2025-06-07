s=input('Inserire una stringa:')
while s!=s.lower() or s.isalpha()==False:
    print(s[0])
    print(s[-1])
    s=input('Inserire una stringa:')
else:
    print(s[0])
    print(s[-1])
    
    
