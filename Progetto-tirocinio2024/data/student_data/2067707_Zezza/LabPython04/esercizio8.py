s=input('inserisci stringa: ')
r=input('inserisci stringa: ')
while s[-1]!=r[0] and r[-1]!=s[0]:
    if r[-1]!=s[0]:
        s=input('inserisci stringa: ')
    if r[-1]!=s[0]:
        r=input('inserisci stringa: ')
if s[-1]==r[0]:
    print(s,r)
elif r[-1]==s[0]:
    print(r,s)
