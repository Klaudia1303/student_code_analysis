s='C'
while s.islower()==False:
    s=input('inserisci una stringa (solo caratteri alfabetici minuscoli per terminare): ')
    print(s[0],s[len(s)-1], sep='')