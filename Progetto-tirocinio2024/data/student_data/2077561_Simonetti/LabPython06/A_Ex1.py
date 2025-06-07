n1=int(input('Please enter a number: '))
n2=int(input('Please enter a number: '))
for num in range(n1,0,-1):
    if n1%num==0 and n2%num!=0:
        print(num)
