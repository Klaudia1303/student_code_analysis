somma_negativi=0
n=(input('inserire numero intero: ''(per terminare: *)'))
while n!='*':
    if int(n)<0:
        somma_negativi= somma_negativi+int(n)
    n=(input('inserire numero intero: ''(per terminare: *): '))
    
print(somma_negativi)
        
