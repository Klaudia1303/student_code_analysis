n1= float(input('inserisci numero intero'))
n2= float(input('inserisci numero intero'))
k=0
if n2==0 or n1==0:
    print(0)
else:
    if n2<0 and n1<0 or n1>0 and n2>0:
        n2=abs(n2)
        n1=abs(n1)
        while n2!=0:
            k=k+n1
            n2=n2-1
        print(k)
    else:
        if n2<0:
            while n1!=0:
                k=k+n2
                n1=n1-1
            print(k)
        else:
            if n1<0:
                while n2!=0:
                    k=k+n1
                    n2=n2-1
                print(k)
            
