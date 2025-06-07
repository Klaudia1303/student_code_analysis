n=int(input('inserisci intero: '))
s=int(input('inserisci intero: '))
k=0
risultato=0
if s==0:
    print(0)
if s==1:
    print(n)
if s==-1:
    print(-n)
else:
    if s<0 and s!=-1:
        while k!=abs(s) :
            risultato=risultato+n
            k=k+1
        print(-risultato)
    if s>0 and s!=1:
        while k!=s:
            risultato=risultato+n
            k=k+1
        print(risultato)
