n=int(input('inserire base triangolo: '))
s='*'
f=' '
g=int(n-1)
for i in range(1,n+1,2):
        print(f*g+s*i+f*g)
        g -= 1
