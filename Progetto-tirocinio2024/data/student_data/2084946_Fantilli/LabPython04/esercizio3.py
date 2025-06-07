n = input()
c = '*'
c = str(c)
i=0
s=0
while n != c:
    n = int(n)
    if n <= 0:
        s+=n
    elif n == c:
        n = str(n)
    n = input()
    i+=1
print("somma interi negativi: ", s)
