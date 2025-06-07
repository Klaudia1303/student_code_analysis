s=input('inserire stringa: ')
x=0
for i in range(len(s)):
    distanza=s.rfind(s[i])-s.find(s[i])
    print(s[i], distanza)
    if distanza>x:
        x=distanza
print(x)
