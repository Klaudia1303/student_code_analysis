s=input('Inserisci una stringa(tutto minuscolo per terminare): ')
while s.isalpha() and s.islower()==False:
    print(s[0]+s[len(s)-1])
    s=input('Inserisci una stringa(tutto minuscolo per terminare): ')
print(s[0]+s[len(s)-1])