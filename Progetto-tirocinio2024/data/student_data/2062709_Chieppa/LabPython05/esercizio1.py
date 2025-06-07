s1=input('inserire stringa 1: ')
s2=input('inserire stringa 2: ')
s3=''
if len(s1)==len(s2):
    for i in range(len(s1)):
        s3=s3+s1[i]+s2[i]
print(s3)
