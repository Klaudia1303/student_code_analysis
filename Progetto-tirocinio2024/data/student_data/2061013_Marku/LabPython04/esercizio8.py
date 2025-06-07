s='a'
r='b'

while s[-1]!=r[0] and r[-1]!=s[0]:
    if s[-1]!=r[0]:
        s=input('inserire una stringa: ')
    if r[-1]!=s[0]:
        r=input('inserire una stringa: ')
if s[-1]==r[0]:
    print(s,r)
elif r[-1]==s[0]:
    print(r,s)
