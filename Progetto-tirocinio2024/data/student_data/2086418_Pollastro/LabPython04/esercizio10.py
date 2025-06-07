s1=str(input('inserire stringa: '))
s2=str(input('inserire stringa: '))
s3=str(input('inserire stringa: '))
while len(s1)+len(s2)!=len(s3):
    s1=s2
    s2=s3
    s3=str(input('inserire stringa: '))
print(s1,s2,s3)
