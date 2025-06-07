c=int(input('inserire un numero intero maggiore o uguale di 0: '))
fattoriale=1
if(c==0 or c==1):
    print(fattoriale)
elif(c>1):
    i=2
    while(i<=c):
        fattoriale=fattoriale*i
        i=i+1
print(fattoriale)
