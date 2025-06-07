i=0
x=True

while x:
    n=int(input("scrivi un intero: "))
    if n==0:
        print(i)
        x=False
    elif n%3==0:
        i+=n
    elif n%3!=0:
        ''
