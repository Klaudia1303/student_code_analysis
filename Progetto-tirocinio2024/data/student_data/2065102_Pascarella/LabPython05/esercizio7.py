s=input()
n=1
falso="False"

for i in range(len(s)-1):
    while n<=len(s)-1:
        if ord(s[i])==ord(s[n]) and i!=n:
            falso="True"
        n+=1
    n=1
print(falso)
