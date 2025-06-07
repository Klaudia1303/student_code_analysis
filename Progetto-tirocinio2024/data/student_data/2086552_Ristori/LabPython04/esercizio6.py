n1=int(input("Inserire il primo numero intero:"))
n2=int(input("Inserire il secondo numero intero:"))
b=True
moltiplicazione=0
while b:
    if n1>=1 and n2>=1:
        moltiplicazione=moltiplicazione+n1
        n2=n2-1
        if n2==0:
            b=False
            print(moltiplicazione)
    elif n1<=-1 and n2<=-1:
        n1=str(n1)
        n1=n1.replace("-","+")
        n1=int(n1)
        moltiplicazione=moltiplicazione+n1
        n2=str(n2)
        n2=n2.replace("-","+")
        n2=int(n2)
        n2=n2-1
        if n2==0:
            b=False
            moltiplicazione=str(moltiplicazione)
            print("-"+moltiplicazione)
    elif n1>=1 and n2<=-1:
        moltiplicazione=moltiplicazione+n1
        n2=n2+1
        if n2==0:
            b=False
            moltiplicazione=str(moltiplicazione)
            print("-"+moltiplicazione)
    elif n1<=-1 and n2>=1:
         moltiplicazione=moltiplicazione-n1
         n2=n2-1
         if n2==0:
             b=False
             moltiplicazione=str(moltiplicazione)
             print("-"+moltiplicazione)
    elif n1==0 or n2==0:
        print(0)
        b=False
        
    
