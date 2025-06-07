n=int(input('Inserire un numero positivo maggiore di 0: '))
i=1
while n>0 and i<=n:
    if n%i==0:
        print(i)
        i+=1
    else:
        i+=1
