i=0
n=str(input("Inserire un intero: "))
while not (str(n)=='*'):
    if(int(n)<0):
        i=i+1
    n=str(input("Inserire un intero: "))
print(i)
