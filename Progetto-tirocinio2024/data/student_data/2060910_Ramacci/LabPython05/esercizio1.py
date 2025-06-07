z=input("inserire una stringa: ")
s=input("inserire una stringa: ")
if len(z)==len(s):
    for i in range(len(s)):
        print(z[i]+s[i],end="")
