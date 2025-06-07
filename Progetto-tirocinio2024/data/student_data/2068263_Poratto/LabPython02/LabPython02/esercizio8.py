a=int(input('inserisci a: '))
b=int(input('inserisci b: '))
c=int(input('inserisci c: '))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    if a==b and a==c and b==c:
        print('equilatero')
    elif a==b or b==c or a==c:
        print('isoscele')
    else:
        print('scaleno')
else:
    print('input non valido')
