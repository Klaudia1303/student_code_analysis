n=int(input('inserire numero base triangolo isoscele: '))

for i in range (1,n+1,2):
    s=(n-1)/2
    s=int(s)
    print((' '*s)+('*'*i)+(' '*s))
