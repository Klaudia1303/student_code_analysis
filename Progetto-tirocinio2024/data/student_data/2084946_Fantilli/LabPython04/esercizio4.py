s=0
n = input()
n = int(n)
if n%3==0:
    s+=n
i=0
while n != 0:
    n = input()
    n = int(n)
    if n%3==0:
        s+=n
    i+=1
    if n == 0:
        print("somma degli interi divisibili per '3' =", s)
