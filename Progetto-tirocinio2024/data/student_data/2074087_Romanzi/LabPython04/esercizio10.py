s1=str(input('Stringa '))
s2=str(input('Stringa '))
j=True
while j:
    s3=str(input('Stringa '))
    if len(s1)+len(s2)==len(s3):
        print(s1+' '+s2+' '+s3)
        j=False
    else:
        s1=s2
        s2=s3
