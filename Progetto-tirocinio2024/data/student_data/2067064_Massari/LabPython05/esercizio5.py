s=input('inserire una parola: ')
n=int(input('inserire un intero positivo: '))
conto=0
for i in range(len(s)-n):
    if s[i]==s[i+n]:
        conto+=1
        
if conto>=1:
    print('True')
else:
    print('False')
