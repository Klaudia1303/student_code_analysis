n=input("inserire un numero intero:")
i=0
while n!="*":
    if int(n)<0:
        i+=int(n)
    n=input("inserire un numero intero:")
print(i)
