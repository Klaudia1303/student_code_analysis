n=int(input("inserisci un numero maggiore di 2 "))
if n>2:
    a=1
    while a!=n+1:
        if a%2==0:
            print(a)
            a=a+1
        else:
            a=a+1
else :
    print("a è minore di 2")
    
