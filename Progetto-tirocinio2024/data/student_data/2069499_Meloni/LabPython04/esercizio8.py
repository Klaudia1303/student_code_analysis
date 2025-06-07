s_1=input('Inserisci la stringa ')
s_2=input('Inserisci la stringa ')
while s_1[-1]!=s_2[0]:
    s_1=s_2
    s_2=input('Inserisci la stringa ')
if s_1[-1]==s_2[0]:
    print(s_1,' ',s_2)
