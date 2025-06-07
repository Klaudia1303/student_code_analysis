n = int(input('inserisci intero: '))

for i in range(n):
    s = ''
    for j in range(n):
        #print(j)
        if i == 0 or j == 0 or j == n-1 or i == n-1 or j == i or j == n-1-i:
            #print(abs(i-j), j, i)
            s += '*'
        else:
            s += ' '
    print(s)
