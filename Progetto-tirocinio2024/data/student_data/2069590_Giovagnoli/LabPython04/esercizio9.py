n=int(input("Inserire un numero intero maggiore a 0: "))
if n>0:
    contatore=0
    fibonacci=0
    fibonacci1 = 1
    fibonacci2 = 1
    while contatore<n:
        if contatore>=2:
            fibonacci = fibonacci1+fibonacci2
            fibonacci1=fibonacci2
            fibonacci2 = fibonacci
        else:
            print(fibonacci1,"\n")
            contatore+=1
            continue
        print(fibonacci,"\n")
        contatore+=1