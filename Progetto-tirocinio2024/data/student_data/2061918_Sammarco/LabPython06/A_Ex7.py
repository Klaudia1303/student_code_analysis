s1=input("inserisci una stringa:")
s2=input("inserisci una seconda stringa:")
r=0
c=""
if s1!="" and s2!="":
    for i in range(len(s1)):
        for j in range(len(s1)):
            m=s1[i:j+1]
            if m in s2 and len(m)>r:
                r=len(m)
                c=m
print(c)
                
                
