x=input('inserisci una stringa contenente almeno due caratteri: ')
n=int(input('inserisci un intero positivo: '))
for i in range(len(x)-n):
    if x[i]==x[i+n]:
        print('True')
if x[i]!=x[i+n]:
    print('False')


    
