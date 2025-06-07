s1=input('inserire stringa')
s2=input('inserire stringa')
s3=''
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if s1[i]==s2[j]:
            s3+=s1[i]
            i+=1
        elif s1[i]!=s2[j]:
            break
            
print(s3)
