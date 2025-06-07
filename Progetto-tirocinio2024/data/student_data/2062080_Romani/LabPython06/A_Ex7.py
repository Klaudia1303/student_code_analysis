s1=input('Inserire stringa: ')
s2=input('Inserire stringa: ')
s3=''
for i in range(0,len(s1) - 1):
    for j in range(0,len(s2) - 1):
        if s1[i]==s2[j]:
            s3+=s1[i]
            i+=1
        elif s1[i]!=s2[j]:
            break

print(s3)
