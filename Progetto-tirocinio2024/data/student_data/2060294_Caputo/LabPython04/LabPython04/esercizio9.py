num=int(input('inserisci un numero: '))
i=1
a=0
b=1
fibonacci=0
print(1)
while i<num:
    i=i+1
    fibonacci=a+b
    print(fibonacci)
    a=b
    b=fibonacci
    
