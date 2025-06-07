n=int(input('inserire lunghezza del lato del quadrato: '))
print(n*'*')
for i in range(1,n-1):
    print('*'+(n-2)*' '+'*')
print(n*'*')
