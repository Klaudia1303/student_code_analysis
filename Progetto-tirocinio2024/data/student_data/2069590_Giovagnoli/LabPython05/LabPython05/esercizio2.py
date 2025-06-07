s= input("Inserire una stringa: ")
n=int(input("Inserire un intero: "))
if n>0:
    s_finale=""
    for i in range(len(s)):
        s_finale=s_finale+(s[i]*n)
    print(s_finale)