v=True
s2=""
s3=""
while v:
    
    s1=input("inserire una stringa:")
    if s1=="":
        print("input non valido")
    else:
        
        if s2=="":
            s2=s1
        else:
            if s3=="":
                s3=s2
                s2=s1
            else:
                if len(s1)==len(s2)+len(s3):
                    print(s3,s2,s1)
                    v=False
                else:
                    s3=s2
                    s2=s1
