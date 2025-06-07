a=int(input('immetere un numero maggiore di 0 '))
b=int(1)
while a>0:
    if a//b>0 and a%b==0:
        print(b)
    b=b+1
