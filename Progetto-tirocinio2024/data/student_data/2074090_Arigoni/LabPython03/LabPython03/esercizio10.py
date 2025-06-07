
n=int(input("Inserisci un numero>> "))

x=2
y=2
while x<=n:
    while y<=n:
        if x%y==0 and x!=y:
            y=x+1
        elif y==x:
            print(x)
            y=x+1
        else:
            y=y+1
    y=2
    x=x+1
