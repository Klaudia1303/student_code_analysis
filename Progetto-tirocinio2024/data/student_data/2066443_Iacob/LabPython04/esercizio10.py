s1 = str(input('Insert string: '))
s2 = str(input('Insert string: '))
s3 = str(input('Insert string: '))
while len(s1)+len(s2)!=len(s3):
    s1 = s2
    s2 = s3
    s3 = str(input('Insert string: '))
print(s1,s2,s3)
