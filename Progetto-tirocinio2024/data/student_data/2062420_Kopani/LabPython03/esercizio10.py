n=int(input('Inserisci un numero: '))
p=2
while n>=p:
        d=2
        k=0
        while d<=p/2:
            if p%d==0:
                k+=1
            d+=1
        if k==0:
            print(p)
            p+=1
        else:
            p+=1