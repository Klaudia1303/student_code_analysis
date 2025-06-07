n=int(input('inserire lunghezza lato quadrato>=3 : '))
if n>=3 and n%2!=0:
    print(n*'*')
    for i in range(1,n-1):
        print('*'+(n-2)*' '+'*')
    print(n*'*')
