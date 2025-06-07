s=input('inserisci una stringa con almeno due caratteri:')
n=int(input('inserisci un intero positivo:'))
i=0
corretto=True
while(i+n)<len(s):
    if s[i]==s[i+n] and corretto:
        print(True)
        corretto=False
    i+=1
if corretto==True:
    print(False)
