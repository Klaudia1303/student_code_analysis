s1 = input()
s2 = input()
a = True
while a:
    s3 = input()
    if len(s1)+len(s2)==len(s3):
        print(s1, s2, s3)
        a = False
    s1=s2
    s2=s3
