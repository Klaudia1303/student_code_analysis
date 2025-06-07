running=True
v=0
k=0
w=0
while running:
    s1=input("Inserire una stringa: ")
    v=len(s1)
    if k+w==v:
        running=False
    if running!=False:
        s2=input("Inserire una stringa: ")
        k=len(s2)
        if w+v==k:
            running=False
    if running!=False:
        s3=input("Inserire una stringa: ")
        w=len(s3)
        if v+k==w:
            running=False
    
if k+w==v:
    print(s2,s3,s1)
if w+v==k:
    print(s3,s1,s2)
if v+k==w:
    print(s1,s2,s3)

