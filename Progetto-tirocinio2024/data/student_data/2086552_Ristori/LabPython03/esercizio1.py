var1=int(input("Inseire un intero strettamente maggiore di 2:"))
while var1<=2:
    print("Il numero inserito non è corretto")
    var1=int(input("Inserire nuovamente un numero maggiore di 2:"))
n=0
if var1%2==0:
    while n<var1:
        print(n+2)
        n=n+2
elif var1%2==1:
    while n<var1-1:
        print(n+2)
        n=n+2


