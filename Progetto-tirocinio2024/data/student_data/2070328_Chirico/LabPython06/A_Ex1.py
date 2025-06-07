n1 = int(input('primo numero = '))
n2 = int(input('secondo numero = '))

for i in range (n1,0,-1):
    if n1%i == 0:
        if n2%i != 0:
            print(i)
