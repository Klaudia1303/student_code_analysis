s_1=input('Inserisci la stringa ')
s_2=input('Inserisci la stringa ')
s_3=input('Inserisci la stringa ')
while (len(s_1)+len(s_2))!=len(s_3):
    s_1=s_2
    s_2=s_3
    s_3=input('Inserisci la stringa ')
if (len(s_1)+len(s_2))==len(s_3):
    print(s_1,' ',s_2,' ',s_3)
