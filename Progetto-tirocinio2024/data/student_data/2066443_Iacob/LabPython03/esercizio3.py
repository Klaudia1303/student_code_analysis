stop = False
while not stop:
    n = int(input('Insert number: '))
    if n%5==0:
        print(n//5)
        stop = True
