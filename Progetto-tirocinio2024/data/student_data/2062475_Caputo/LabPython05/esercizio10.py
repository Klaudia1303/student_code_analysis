n = int ( input ("inserire un numero maggiore o uguale a due, n: "))
print ("\n")
for i in range (0, n):
    if i == 0 or i == n-1:
        print ('*' * n, end='')
    else:
        for j in range (0, n):
            if ( j == i or j == (n-1)-i or j == n-1 or j == 0):
                print ('*', end = '')
            else:
                print (' ', end = '')
    print ("\n", end='')
        
