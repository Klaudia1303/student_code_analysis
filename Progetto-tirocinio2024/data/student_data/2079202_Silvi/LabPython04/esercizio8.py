v=True
s2=""
while v:
    s1=input("inserire una stringa:")
    if s1=="":
        print("input non valido")
    else:
        if s2!="":
            if s1[0]==s2[len(s2)-1]:
                v=False
            else:
                s2=s1
        else:
            s2=s1

print(s2,s1)
