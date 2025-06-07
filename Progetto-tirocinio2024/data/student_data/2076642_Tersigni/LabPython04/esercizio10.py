s1=input("s1:")
s2=input("s2")
s3=input("s3")
while len(s3)!=len(s1)+len(s2):
    s1=s2
    s1=s3
    s3=input("s3:")
print(s1,s2,s3)
    
