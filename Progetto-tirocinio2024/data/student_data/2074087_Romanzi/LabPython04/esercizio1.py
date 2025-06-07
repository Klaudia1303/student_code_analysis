k=True
p=0
while k:
    s=str(input('Stringa '))
    p=p+1
    for i in range(len(s)):
        if s[i]=='c':
            for i in range(len(s)):
                if s[i]=='a':
                    k=False
print(p)
