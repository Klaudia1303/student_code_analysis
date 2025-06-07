n=input("inserire una stringa:")
a="a"
b="z"
while b!=a:
    m=n
    n=input("inserire nuova stringa:")
    a=m[-1]
    b=n[0]
print(m,n)
