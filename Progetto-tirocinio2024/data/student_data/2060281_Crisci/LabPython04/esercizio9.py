n=int(input("inserisci un intero maggiore di 0: "))
i=2
f=1
g=1
app=0
print(1)
print(1)
while(i<n):
    app=f+g
    f=g
    g=app
    i=i+1
    print(g)
