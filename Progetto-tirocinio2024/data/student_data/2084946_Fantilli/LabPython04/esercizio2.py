n = input()
c = '*'
c = str(c)
i=0
s=0
while n != c:
    n = int(n)
    if n <= 0:
        s+=1
        i+=1
    elif n > 0:
        i+=1
    n = input()
if n == c:
    n = str(n)
print("interi positivi inseriti: ", i-s)
