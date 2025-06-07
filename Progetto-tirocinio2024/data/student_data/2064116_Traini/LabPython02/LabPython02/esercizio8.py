a=int(input('inserire un numrero intero: '))
b=int(input('inserire un numrero intero: '))
c=int(input('inserire un numrero intero: '))
#Si definisce triangolo scaleno un triangolo i cui tre lati non sono congruenti
#si definisce triangolo isoscele un triangolo che possiede due lati congruenti.
#un triangolo equilatero ha i suoi tre lati congruenti tra loro
if a<=0 and b<=0 and c<=0 or a>b+c or b>a+c or  c>a+b:
    print('input non valido')
elif a!=b!=c and a!=c!=b:
    print('scaleno')
elif  a==b!=c or a==c!=b or b==c!=a:
    print('isoscele')
    
    

elif a==b and b==c and c==a:
    print('equilatero')
    
    
    

    
    
