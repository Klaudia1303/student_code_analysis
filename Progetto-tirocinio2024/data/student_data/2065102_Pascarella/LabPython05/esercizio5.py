s=input()
n=int(input())
falso="False"

for i in range(len(s)-n):
    if s[i]==s[i+n]:
        falso="True"
print(falso)
