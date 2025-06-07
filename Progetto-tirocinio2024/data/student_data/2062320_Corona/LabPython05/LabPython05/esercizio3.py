s1= str(input())
s2 = str(input())

for c in s1:
    if c not in s2:
        print(c,end='')