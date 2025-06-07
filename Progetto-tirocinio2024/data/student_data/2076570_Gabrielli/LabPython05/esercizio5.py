s=input('inserisci una stringa con almeno due caratteri: ')
n=int(input('inserisci numero positivo: '))
stessocarattere= not True

for i in range(len(s)-n):
    if s[i]==s[i+n]:
        stessocarattere=True
if  stessocarattere==True:
    print('True')
else:
    print('False')
