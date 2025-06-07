s=input("inserire una stringa: ")
n=0
for i in range(0,1):
    if s.rfind(s[i])-i>n:
        n=s.rfind(s[i])-i
print(n)
