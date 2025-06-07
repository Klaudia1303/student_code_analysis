s=input('Inserisci una stringa: ')
n=int(input('Inserisci un numero intero positivo: '))
i=0
corretto=True
while (i+n)<len(s):
    if s[i]==s[i+n] and corretto:
        print(True)
        corretto=False
    i+=1
if corretto==True:
    print(False)