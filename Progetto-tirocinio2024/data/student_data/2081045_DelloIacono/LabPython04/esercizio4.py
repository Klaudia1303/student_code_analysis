somma=0
c=int(input('inserire un intero'))
while not(int(c)==0):
    if int(c)%3==0:
        somma=somma+c
    c=int(input('inserire un intero'))
    
print(somma)
