i=0
x=True

while x:
    n=input("scrivi un intero: ")
    if n=='*':
        print(i)
        x=False

    elif n.isdecimal()>0:
        ''
    elif n.isdecimal()<=0:
        i+=int(n)
