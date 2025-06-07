n = int(input("Inserire un numero intero: "))
primo = False
i=2
while i<n:
    if (n%i)==0:
        print("Numero non primo!")
        break
    else:
        if i==(n-1):
            print("Numero primo")
            break
        i+=1
if n==2 or n==1:
    print("Numero primo")
    