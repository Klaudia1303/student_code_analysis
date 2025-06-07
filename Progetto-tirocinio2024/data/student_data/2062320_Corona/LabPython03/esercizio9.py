w = True

while w:
    n= int(input())
    k = 2
    if n % k == 0:
        print('non primo')
    else:
        print('primo')
    k = k+2