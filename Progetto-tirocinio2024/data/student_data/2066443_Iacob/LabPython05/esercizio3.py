s1 = str(input('Insert string: '))
s2 = str(input('Insert second string: '))
f=''
for i in s1:
    if i not in s2:
        f = f+i
print(f)
