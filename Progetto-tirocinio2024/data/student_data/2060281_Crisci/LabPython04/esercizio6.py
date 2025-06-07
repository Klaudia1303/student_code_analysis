n1=int(input("Inserire un intero: "))
n2=int(input("Inserire un intero: "))
i=0
somma=0
if(n2>0):
    while(i<n2):
        somma=somma+n1
        i=i+1
if(n2<0):
    while(i>n2):
        somma=somma+n1
        i=i-1
    if(n1>0):
        somma=-somma
print(somma)
