s=input('inserisci stringa:')
n=int(input('inserisci intero positivo:'))
corretto=True
for i in range(len(s)-n):
    if s[i]==s[i+n] and corretto:
        print('True')
        corretto=False
if corretto==True:
    print('False')
    

