n=int(input('inserisci un intero: '))
i=2
x=1
while 2<=i<=n:
    if i==2:
        print(2)
    x=int(2)
    while x<i/2 and i%x!=0:
        x+=1   
    if i%x!=0:
        print(i)
   
    i+=1
