s1 = str(input('Insert string: '))
s2 = str(input('Insert string: '))
a=''
b=''
for i in range(len(s1)):
    for k in range(len(s2)):
        if s1[i]==s2[k]:
            b=''
            for w in range(len(s2)-k):
                if s1[i+w]==s2[k+w]:
                    b=b+s1[i+w]
                else:
                    break
            if len(b)>len(a):
                a=b
print(a)
