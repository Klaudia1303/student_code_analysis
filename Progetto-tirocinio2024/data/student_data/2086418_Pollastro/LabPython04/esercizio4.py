Somma=0
n=(input('inserire numero intero: ''(per terminare: *)'))
while n!='*':
    if int(n)%3==0:
        Somma= Somma+int(n)
    n=(input('inserire numero intero: ''(per terminare: *): '))
    
print(Somma)
        
