s3 = input('Inserire una stringa: ' )
s1 = ''
s2 = ''

while (len(s1)+len(s2))!=len(s3):
    print(len(s1), len(s2), len(s3))
    s1 = s2
    s2 = s3
    s3 = input('Inserire una stringa: ' )
print(s1, s2, s3)
