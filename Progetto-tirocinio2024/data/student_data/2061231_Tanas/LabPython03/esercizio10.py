n = 0
while n <= 1:
    n = int(input('n (>1): '))

nn = 2
while nn <= n:
    i = 2
    primo = True
    while i <= nn//2:
        if nn % i != 0:
            i += 1
        else:
            primo = False
            break
    
    if primo: 
        print(nn)
    nn += 1
