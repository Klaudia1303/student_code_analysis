n = int(input("Inserire lato del quadrato: "))
print('*'*n)
l = n - 3
for i in range(n-2):
    
    print('*', end = "")
    for j in range(n-2):
        if(j == i or j == l):
            print('*', end = "")
        else:
            print(' ', end = "")
    print('*')
    l = l - 1
print('*'*n)
