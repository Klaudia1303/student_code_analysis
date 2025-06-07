s1=str(input('s1='))
s2=str(input('s2='))
n=int(input('intero='))
s=''
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if s1[i]==s2[j] and s1.find(s1[i])-s2.find(s2[j])<=n:
            s=s+s1[i]
print(s)            
            
