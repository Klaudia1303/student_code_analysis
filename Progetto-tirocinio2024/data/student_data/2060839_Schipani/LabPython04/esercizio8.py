s=input('inserisci una stringa ')
r=input('inserisci una stringa ')
while s[-1]!=r[0] and r[-1]!=s[0]:
    if r[-1]!=s[0]:
        s=input('inserisci una stringa ')
    if r[-1]!=s[0]:
        r=input('inserisci una stringa ')
if s[-1]==r[0]:
    print(s,r)
elif r[-1]==s[0]:
    print(r,s)
