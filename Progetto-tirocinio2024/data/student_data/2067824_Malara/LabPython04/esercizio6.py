n1=int(input('inserire numero ' ))
n2=int(input('inserire numero '))
somma=n1
a=1

while a<abs(n2):
    somma=somma+n1
    a+=1
if n2<0:
        print(-somma)
else:
        print(somma)
