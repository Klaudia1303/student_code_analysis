s1=input("immetti stringa: ")
s2=input("immetti stringa: ")
s3=input("immetti stringa: ")
while len(s1)+len(s2)!=len(s3):
    s1=s2
    s2=s3
    s3=input("immetti stringa: ")
    
print(s1,s2,s3)
