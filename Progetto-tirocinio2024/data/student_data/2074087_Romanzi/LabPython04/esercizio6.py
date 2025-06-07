n=int(input('Intero 1 '))
h=int(input('Intero 2 '))
s=0
for i in range(1,abs(h)+1):
    s=s+n
if h>=0:
    print(s)
else:
    print(-s)
