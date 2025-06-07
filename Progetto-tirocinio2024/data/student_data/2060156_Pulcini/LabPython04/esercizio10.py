s=input('inserire una stringa:')
l1=len(s)
finito=False
while not finito:
    s1=s
    s=input('inserire una stringa:')
    s2=len(s)
    s2=s
    s=input('inserire una stringa:')
    s3=len(s)
    s3=s
    if l1+l2==l3:
        finito=False
    else:
        l1=len(s)
print(s1,s2,s3)

