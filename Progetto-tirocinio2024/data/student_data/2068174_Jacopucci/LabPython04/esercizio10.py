c=0
s3=input('inserire un stringa: ')
s2=input('inserire un stringa: ')
s1=input('inserire un stringa: ')
cs3=len(s3)
cs2=len(s2)
cs1=len(s1)
while (c!=1):
    if(cs3+cs2!=cs1):
        s3=s2
        s2=s1
        s1=input('inserire un stringa: ')
        cs3=len(s3)
        cs2=len(s2)
        cs1=len(s1)
    else:
        c+=1
print(s3+' '+s2+' '+s1)
