n=int(input('inserire il lato del quadrato:'))
if n%2!=0 and n>=3:
    print('*'*n)
    for i in range(n-2):
        print('*'+' '*(n-2)+'*')
    print('*'*n)
