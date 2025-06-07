i=0
s1=input('Inserire una stringa:')
s2=input('Inserire una stringa:')
s3=input('Inserire una stringa:')
while (len(s1)+len(s2))!=len(s3):
    s1=s2
    s2=s3
    s3=input('Inserire una stringa:')
print(s1, s2, s3)
    
