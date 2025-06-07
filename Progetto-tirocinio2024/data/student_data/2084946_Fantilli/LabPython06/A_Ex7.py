s1=input()
s2=input()
s3=0
for i in range(len(s2)):
    for j in range(i+1,len(s2)):
        for k in range(len(s2)):
            if s1[i:j]==s2[i+k:j+k] and len(s1[i:j])>s3:
                s3=len(s1[i:j])
                print(s1[i:j])
