s1=input()
s2=input()
y=''
for x in range (len(s1)):
    for y in range (len(s1)+1):
        if s1[x:y] in s2 and len(s1[x:y])>len(y):
            y=s1[x:y]
print(y)

