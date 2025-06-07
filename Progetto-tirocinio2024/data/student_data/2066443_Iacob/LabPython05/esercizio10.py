n = int(input('Insert number: '))
for i in range(n):
    for x in range(n):
        if (i==x or (i+x==(n-1))) or ((i==0)or (x==0)) or ((i==(n-1)) or (x==(n-1))):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
