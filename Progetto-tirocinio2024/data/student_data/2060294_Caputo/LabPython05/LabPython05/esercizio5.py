s=input('inserisci una stringa con almeno 2 caratteri: ')
n=int(input('inserisci un numero positivo: '))
controllo= False
for i in range(len(s) - n):
    if s[i] == s[i+n]:
        controllo= True
print('ci sono due caratteri uguali a distanza massima n? ', controllo)
