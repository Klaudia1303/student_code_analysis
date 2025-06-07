n=int(input("base: "))
for i in range(1,n+1,2):
    print(' '*int((n-i)/2)+'*'*i)
