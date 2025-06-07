a=int(input('inserire numero intero_1:'))
b=int(input('inserire numero intero_2:'))
c=int(input('inserire numero intero_3:'))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('il triangolo è equilatero')
    elif a!=b!=c:
        print('il trinagolo è scaleno')
    elif (a==b and a,b!=c) or (a==c and a,c!=b) or (c==b and c,b!=a):
        print('il triangolo è isoscele')
else:
    print('input non valido')
