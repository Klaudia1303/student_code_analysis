s=input('inserisci stringa: ')
n=int(input('inserisci distanza: '))
c=0
for i in range(len(s)-n):
    if s[i]==s[i+n]:
        print('True')
        c=1
if c==0:
    print('False')
