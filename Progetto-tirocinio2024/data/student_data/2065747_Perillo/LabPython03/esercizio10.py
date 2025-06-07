d=int(input("inserire un numero maggiore di 1 "))
g=1
c=str(1)

while g<d:
    l=1
    g=g+1
    b=1
    while b<=g:
        if g%b==0:
            l=str(l)+str(b)
        
            if l=="11"+str(g):
                print(g) 
        b=b+1


    
