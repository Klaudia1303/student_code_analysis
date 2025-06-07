s=input('inserisci una stringa: ')

c=0
a=''

for i in range(len(s)):
    rip=0
    for k in range(i, len(s)):
        if s[k]!=s[i]:
            break
        rip+=1
    if rip>=c:
        a=s[i]
        c=rip
print(a,c)
