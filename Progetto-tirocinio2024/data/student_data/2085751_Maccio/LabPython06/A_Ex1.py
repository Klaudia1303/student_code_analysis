n1=int(input("Inserire un numero intero maggiori di 0:  "))
n2=int(input("Inserire un altro numero intero maggiori di 0:  "))
i=n1
if n1<0 or n2<0:
    print("Errore, input non corretto")
else:
    while i>0:
        r=n1%i
        if n2%i!=0 and r==0:
            print(i)
        i=i-1
