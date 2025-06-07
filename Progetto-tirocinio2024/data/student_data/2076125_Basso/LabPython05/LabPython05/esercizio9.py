
a=int(input("Inserire lato quadrato:\t"))

for i in range(1,a+1):
    if i==1 or i==a:
        print('*'*a)
    else:
        print('*','*', sep=' '*(a-2))
