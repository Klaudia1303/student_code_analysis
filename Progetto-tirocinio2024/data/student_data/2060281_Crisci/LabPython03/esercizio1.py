n=int(input("Inserire un numero maggiore di 2: "))
if(n%2==0):
    while(n>=2):
        print(n)
        n=n-2
else:
    n=n-1
    while(n>=2):
        print(n)
        n=n-2
