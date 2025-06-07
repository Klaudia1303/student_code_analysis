s = str(input('Insert string: '))
pal=0
for l in range(len(s)):
    if s[l]!=s[-l-1]:
        break
    elif s[l]==s[-l-1]:
        pal=pal+1
print(pal)
