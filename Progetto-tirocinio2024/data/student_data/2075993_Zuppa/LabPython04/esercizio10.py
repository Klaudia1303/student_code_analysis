s=False
s1=input('inserire una stringa   ')
s2=input('inserire una stringa   ')
s3=input('inserire una stringa   ')
while not s:
    if len(s1)+len(s2)==len(s3):
        print(s1,s2,s3)
        s=True
    if not s:
        s1=input('inserire una stringa   ')
    if len(s2)+len(s3)==len(s1):
        print(s2,s3,s1)
        s=True
    if not s:
        s2=input('inserire una stringa   ')
    if len(s3)+len(s1)==len(s2):
        print(s3,s1,s2)
        s=True
    if not s:
        s3=input('inserire una stringa   ')
