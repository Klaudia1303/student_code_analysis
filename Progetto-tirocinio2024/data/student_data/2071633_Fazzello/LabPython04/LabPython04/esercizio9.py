##9)Scrivere un programma python che chiede in input all’utente un intero n maggiore di 0 e stampa uno per
##riga i primi n numeri della successione di Fibonacci. I primi due numeri della successione di Fibonacci
##sono 1 ed 1, ed ogni numero successivo è dato dalla somma dei due precedenti. Quindi avremo: 1 1 2 3 5
##8 13 21 34...
##Esempio:
##Inserendo l’intero “6”, il programma stampa “1”, a capo “1”, a capo “2”, a capo “3”, a capo “5”, a capo
##“8”.

n=int(input('inserisci numero maggiore di 0: '))
p=0
m=1
q=0
z=0
print('1')
for i in range(n):
    z=z+1
    q=p+m
    p=m+q
    m=q+p
    if z<=n:
        z=z+1
        print(q)
        print('z',z)
    elif z<=n:
        z=z+1
        print(p)
        print('z',z)
    elif z<=n:
        z=z+1
        print(m)
        print('z',z)

    
