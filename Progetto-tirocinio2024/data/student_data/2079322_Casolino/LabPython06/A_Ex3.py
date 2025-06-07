#Scrivere un programma Python che stampa la
#tabellina pitagorica dei numeri in base ottale.
#Usare due cifre, e.g., 02x04=10.

n=0
for i in range(8):
    for u in range(8):
        n=i*u
        k=8

        potenza=0
        sol=0
        while n>0:
            quoziente=n//k
            resto=n%k
            n=quoziente
            resto=resto*pow(10,potenza)
            potenza+=1
            sol+=resto
        print('{}x{}={}\t'.format(i, u, sol), end='')
        
