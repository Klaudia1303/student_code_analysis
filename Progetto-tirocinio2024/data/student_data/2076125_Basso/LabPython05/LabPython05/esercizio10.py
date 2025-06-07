
a=int(input("Inserire lato quadrato:\t"))

for y in range(a):
    for x in range(a):
        if x==y or x==0 or y==0 or x==a-y-1 or y==a-x-1 or y==a-1 or x==a-1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

