n=int(input('inserisci numero dispari:'))
j=n//2
for i in range(1,n+1,2):   
    if i%2!=0:
        print(j*' ',i*'*')
        j-=1
