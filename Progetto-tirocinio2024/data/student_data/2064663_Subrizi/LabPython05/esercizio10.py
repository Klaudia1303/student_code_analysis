n=int(input('inserisci il valore del lato di un quadrato: '))

for i in range(n):
        for j in range(n):
                if i==0 or i==n-1:
                        print('*', end='')
                elif j==0 or j==n-1:
                        print('*', end='')
                elif j==i or j==n-1-i:
                        print('*', end='')
                else:
                        print('  ', end='')
        print()
                
