s1=input('Inserisci una stringa: ')
s2=input('Inserisci una stringa: ')
while s1[-1]!=s2[0]:
    s1=s2
    s2=input('Inserisci una stringa: ')

print(s1,s2)
