s=input('inserire una stringa   ')
while len(s)==0:
    s=input('inserire una stringa non vuota  ')
f=s[len(s)-1]
i=''
s1=s
while f!=i:
    f=s[len(s)-1]
    s=input('inserire una stringa   ')
    while len(s)==0:
        s=input('inserire una stringa non vuota  ')
    i=s[0]
    if f!=i:
        s1=s
print(s1,s)
