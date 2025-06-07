n = int(input("Inserisci il lato del quadrato: "))
if n >= 2:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1 or j == i or j == n-1-i:
                print('*', end='')
            else:
                print(' ', end='')

        print()
