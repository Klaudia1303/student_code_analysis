n=int('2')
i=0
d='p'
while d!='*':
    d=input('Inserisci intero o * per terminare ')
    s=str(d)
    if s!='*':
        n=int(d)
        if n>0:
            i+=1
        elif n<0:
            i+=0
print(i)
