s=str(input("Inserire una stringa contenente almento due caratteri:"))
n=int(input("Inserire un numero intero positivo:"))
b=0
for i in range(len(s)):
    if s.count(s[i])==2:
        find=s.find(s[i])
        rfind=s.rfind(s[i])
        if rfind-find==n:
            b="True"
if b=="True":
    print("True")
else:
    print("False")
