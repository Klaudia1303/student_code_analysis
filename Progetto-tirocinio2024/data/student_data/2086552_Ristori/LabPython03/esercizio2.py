var1=int(input("Inserire un numero intero maggiore di zero:"))
while var1<=0:
    print("Il numero inserito non è corretto")
    var1=int(input("Inserire nuovamente un numero intero maggiore di zero:"))
n=1
while n<=var1:
    if var1%n==0:
        print(n)
        n=n+1
    else:
        n=n+1

    
    
    
