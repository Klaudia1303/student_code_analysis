s1=input('s1: ')
s2=input('s2: ')
m=''
for i in range(len(s1)):
    if s1[i] in s2:
        k=i
        s3=''
        for j in range(s2.find(s1[i]),len(s2)):
            if k==len(s1) or s1[k]!=s2[j]:
                break
            else:
                s3+=s2[j]
                k+=1
                if len(s3)>len(m):
                    m=s3
print(m)
                       
