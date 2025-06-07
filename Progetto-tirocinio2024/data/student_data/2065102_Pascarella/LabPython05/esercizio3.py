s1=input()
s2=input()

for i in range(len(s1)):
    if s1[i] not in s2:
        print(s1[i], end="")
