n=input('inserire un numero:')
n=int(n)
while not n%5==0:
    print(n)
    n=int(input('inserire un numero'))
if n%5==0:
    print(n//5)
