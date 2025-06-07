s1=input()
s2=input()
s3=''
n=int(input())
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j] and -n<=(i-j)<=n:
            s3+=s1[i]
print(s3)
