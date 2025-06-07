n=int(input("un intero x compreso tra zero e dieci: "))
m=int(input("un intero y compreso tra zero e dieci: "))
i=1
while(0<=n<=10)and(0<=m<=10)and(0<=i<=10):
    if(i!=n)and(i!=m):
        print(i)
    i+=1
