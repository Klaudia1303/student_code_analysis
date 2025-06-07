n=int(input('inserire un intero maggiore di 3 e dispari   '))
c=(n-1)//2
for i in range(1,n+1,2):
    print(' '*c,'*'*i)
    c-=1
