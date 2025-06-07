s=input('Inserisci una stringa ')
while(s.isalpha()==False or s.islower()==False):
    print(s[0],s[-1])
    s=input('Inserisci la stringa ')
print(s[0],s[-1])
