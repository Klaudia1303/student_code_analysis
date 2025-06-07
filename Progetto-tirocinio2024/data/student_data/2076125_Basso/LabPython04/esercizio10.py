

s1=input("Inserire una stringa:\t")
s2=input("Inserire una stringa:\t")
l1=len(s1)
l2=len(s2)
l3=0

while not (l3 == l1 + l2):
    
    s3=input("Inserire un'altra stringa:\t")
    l3=len(s3)
    l1=len(s1)
    l2=len(s2)
    if l3 == l1 + l2:
        print(s1,s2,s3)

    s1=s2
    s2=s3
    

