n=int(input('Intero maggiore di 0 '))
f=1
s=0
k=0
for i in range(1,n+1):
    print(f)
    k=s
    s=f
    f=k+s
    
