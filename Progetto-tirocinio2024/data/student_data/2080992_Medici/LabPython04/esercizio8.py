i=1
s=str(input('inserire una stringa: '))
s1=s
s=str(input('inserire una stringa: '))
s2=s
while i!=0:
    if s1[0]==s2[-1]:
        print(s2,s1)
        i=0
    else:
        s3=str(input('inserire una stringa: '))
        if s2[-1]==s3[0]:
            print(s3,s2)
            i=0
        s2=s1
        s1=s3
