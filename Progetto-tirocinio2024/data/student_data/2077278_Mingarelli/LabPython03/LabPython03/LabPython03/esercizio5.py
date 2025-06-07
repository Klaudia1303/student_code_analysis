s=input('inserisci una stringa ')
while s.isalpha()!=True or s.islower()!=True:
    print(s[0],s[len(s)-1])
    s=input('inserisci una stringa ')
print(s[0],s[len(s)-1])
