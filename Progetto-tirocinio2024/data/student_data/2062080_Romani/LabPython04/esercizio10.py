s1=input('Inserire stringa: ')
s2=input('Inserire stringa: ')
s3=input('Inserire stringa: ')
while (len(s1)+len(s2))!=len(s3):
    s1=s2
    s2=s3
    s3=input('Inserire stringa: ')
print(s1,s2,s3)
