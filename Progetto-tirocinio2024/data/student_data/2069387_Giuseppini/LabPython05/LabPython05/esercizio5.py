#Scrivere programma che chiede in input all’utente una stringa s contenente almeno due caratteri ed un
#intero positivo n e stampa “True” se nella stringa compaiono 2 lettere uguali a distanza esattamente n,
#“False” altrimenti.

s=input('inserire una stringa(almeno due caratteri): ')
n=int(input('inserisci un intero pos: '))
c=False
d=False
while not c:
    for i in range(0,len(s)):
        if s[i:i+1]==s[i+n:i+n+1]:
            d=True
            c=True
            print(c)
    c=True

if not d:
    print(d)
