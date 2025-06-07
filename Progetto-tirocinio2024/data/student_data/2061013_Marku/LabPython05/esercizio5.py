s=input('inserire stringa di almeno due caratteri: ')
n=int(input('inserire intero positivo: '))
stessocarattere=False

for i in range(len(s)-n):
    if s[i]==s[i+n]:
        stessocarattere=True
if stessocarattere==True:
    print('True')
else:
    print('False')
