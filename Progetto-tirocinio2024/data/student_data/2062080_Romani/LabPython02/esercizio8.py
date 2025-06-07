l1=int(input('Inserire lato 1: '))
l2=int(input('Inserire lato 2: '))
l3=int(input('Inserire lato 3: '))
if l1>0 and l2>0 and l3>0:
    if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
        if l1==l2==l3:
             print('equilatero')
        elif l1!=l2!=l3:
             print('scaleno')
        elif l1==l2 or l1==l3 or l2==l3:
             print('isoscele')
    else:
          print('input non valido')
else:
    print('input non valido')
