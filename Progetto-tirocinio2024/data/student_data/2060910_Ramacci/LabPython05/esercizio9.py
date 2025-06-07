n=int(input("inserire il lato di un quadrato maggiore >=3: "))
print("*"*n)
for i in range(2,n):
    print("*"+(" "*(n-2))+"*")
print("*"*n)
