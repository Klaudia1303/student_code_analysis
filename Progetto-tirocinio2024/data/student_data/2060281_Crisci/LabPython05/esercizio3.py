s1=str(input("Inserire una stringa: "))
s2=str(input("Inserire una stringa: "))
compare=False
for i in s1:
    for j in s2:
        if(i==j):
            compare=True
    if (compare==False):
        print(i, end="")
    compare=False
