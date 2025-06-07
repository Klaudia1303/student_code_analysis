x = float(input('inserisci il numero da moltiplicare: '))
y=float(input('inserisci quante volte dev\'essere ripetuto il numero: '))
k=0
if y==0 or x==0:
    print(0)
else:
    if y<0 and x<0 or x>0 and y>0:
        y=abs(y)
        x=abs(x)
        while y!=0:
            k=k+x
            y=y-1
        print(k)
    else:
        if y<0:
            while x!=0:
                k=k+y
                x=x-1
            print(k)
        else:
            if x<0:
                while y!=0:
                    k=k+x
                    y=y-1
                print(k)

                    
        
                
