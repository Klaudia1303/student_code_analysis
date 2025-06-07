s=str(input("Inserire una stringa:"))
b=True
i=0
while b:
    if s.count('a')>=1 and s.count('c')>=1:
        b=False
        print(i+1)
    else:
        s=str(input("Inserire un'altra stringa:"))
        i=i+1

