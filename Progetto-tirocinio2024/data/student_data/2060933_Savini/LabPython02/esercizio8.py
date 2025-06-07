a= int(input('inserisci numero: '))
b= int(input('inserisci numero: '))
c= int(input('inserisci numero: '))
if a>0 and b>0 and c>0 and a<b+c and b<c+a and c<a+b and a!=b and b!=c and a!=c:
       print('scaleno')
elif a>0 and b>0 and c>0 and a<b+c and b<c+a and c<a+b and a==b and a!=c and b!=c:
    print('isoscele')
elif a>0 and b>0 and c>0 and a<b+c and b<c+a and c<a+b and a==b and a==c and b==c:
    print('equilatero')
else:
    print('input non valido')
