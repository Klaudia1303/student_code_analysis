n = int(input("lato quadrato: "))
while n < 2:
    n = int(input("lato quadrato: "))

for x in range(0, n):
    for y in range(0, n):
        if x == 0 or x == n-1 or y == 0 or y == n-1 or x == y or x == n-1-y:
            print('*',end='')
        else:
            print(' ',end='')
    print('')