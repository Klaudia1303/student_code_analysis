i=1
s1=input("scrivi una stringa: ")
s2=input("scrivi una stringa: ")
s3=input("scrivi una stringa: ")

while i!=2:
    if len(s1)+len(s2)==len(s3) and i!=2:
        print(s1,s2,s3)
        i+=1

    if i!=2:
        s1=input("scrivi una stringa: ")
    if len(s2)+len(s3)==len(s1) and i!=2:
        print(s2,s3,s1)
        i+=1

    if i!=2:
        s2=input("scrivi una stringa: ")
    if len(s3)+len(s1)==len(s2) and i!=2:
        print(s3,s1,s2)
        i+=1
