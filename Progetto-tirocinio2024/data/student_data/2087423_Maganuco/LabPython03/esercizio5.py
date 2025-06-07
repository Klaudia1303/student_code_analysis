s=input('inserisci una stringa')
while (s.isalpha()and s.islower())==0:
    print(s[0],s[-1])
    s=input('inserisci una stringa')
print(s[0],s[-1])
