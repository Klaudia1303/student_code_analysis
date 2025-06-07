n=int(input("inserire un numero intero:"))
i=0
while n!=0:
    if n%3==0:
        i+=n
    n=int(input("inserire un numero intero:"))
print(i)
