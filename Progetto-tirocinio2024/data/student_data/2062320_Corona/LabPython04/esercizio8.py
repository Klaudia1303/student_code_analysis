s1=input('Inserisci stringa:')
s2=input('Inserisci stringa:')
while s1[-1]!=s2[0]:
    s1=s2
    s2=input('Inserisci stringa:')
print(s1,s2)