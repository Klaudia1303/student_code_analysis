s1=input()
s2=input()
mx=""
for i in range(0,len(s1)-1):
    for j in range(len(s1),i+1,-1):
        if(s2.find(s1[i:j])!=-1):
            if (len(s1[i:j])>len(mx)):
                mx=s1[i:j]
print(mx)
