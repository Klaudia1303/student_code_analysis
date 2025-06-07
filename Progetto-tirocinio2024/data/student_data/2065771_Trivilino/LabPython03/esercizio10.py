n=int(input('Inserire un numero intero maggiore di 1: '))
x=2
while x<=n:
    if x>11:
        if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x%11!=0:
            print(x)
            x=x+1
        else:
            x=x+1
    elif x<=11:
        if x==2 or x==3 or x==5 or x==7 or x==11:
            print(x)
            x=x+1
        else:
            x=x+1
