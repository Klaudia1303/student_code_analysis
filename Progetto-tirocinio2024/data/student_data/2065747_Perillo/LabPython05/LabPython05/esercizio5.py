s=input("Inserire la stringa:")
n=int(input("Inserire un numero:"))
a="False"
for i in range(len(s)-n):
    if s[i]==s[i+n]:
        a="True"
print(a)
