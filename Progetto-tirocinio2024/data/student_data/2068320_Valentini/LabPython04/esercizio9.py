n = -1
while n < 0:
    n= int( input( "Inserire un numero n: " ))
somma = 1
Fn = 1
print(str(somma))
print(str(Fn))
for i in range(1,n-1):
    temp=somma
    somma = somma + Fn
    print(str(somma))
    Fn=temp
    
