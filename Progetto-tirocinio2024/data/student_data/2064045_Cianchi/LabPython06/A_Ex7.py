s1=input('inserire una stringa non vuota:')
s2=input('inserire una stringa non vuota:')
caratteri=''
x=''
y=''
for i in range(len(s1)):
    for j in range(len(s2)):
        x=i
        y=j
        if s1[i] in s2:
            caratteri=s1[i]
            x+=1
            y+=1
            if s1[x]==s2[y]:
                caratteri+=s1[x]
print(caratteri)
print(s2[0:4])
                       
                       
                       
        
