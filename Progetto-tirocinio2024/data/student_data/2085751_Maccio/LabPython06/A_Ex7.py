s1=input("Inserire una stringa:  ")
s2=input("Inserire un'altra stringa:  ")
se=''
m=0
for i in range(len(s1)):
    for k in range(len(s1)):
        s=s1[i:k+1]
        if s in s2 and len(s)>m:
            m=len(s)
            se=s
print(se)
