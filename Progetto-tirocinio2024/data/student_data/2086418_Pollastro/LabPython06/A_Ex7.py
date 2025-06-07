s1=input('inserisci stringa non vuota= ')
s2=input('inserisci stringa non vuota= ')
l=int(len(s1))
m=len(s2)
s=''
for i in range (0,l):
    si=''
    st=s1[i:l]
    for c in range (i,l-1):
        if si in s2:
            si=si+s1[c]
            continue
        else:
            continue
        continue
    c1=int(len(s))
    c2=int(len(si))
    if c2>=c1:
        s=si
print (s[0:len(s)-1])
