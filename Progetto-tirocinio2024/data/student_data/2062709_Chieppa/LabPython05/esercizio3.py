s1=str(input('inserire stringa: '))
s2=str(input('isnerire stringa: '))
s3=''
for i in range(0,len(s1)):
    counter=0
    if s2.count(s1[i])>0:
        counter=counter+1
    elif counter==0:
        s3=s3+s1[i]
print(s3)
