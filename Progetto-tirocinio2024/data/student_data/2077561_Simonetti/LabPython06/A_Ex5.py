s=input('Please enter a string: ')
count=1
maxCount=1
for i in range(len(s)):
    if i<len(s)-1:
        if s[i]==s[i+1]:
            count+=1
            char=s[i]
        if s[i]!=s[i+1]:
            count=1
        if count>maxCount:
            maxCount=count
    elif i==len(s)-1:
        if s[i]==s[i-1]:
            count+=1
            char=s[i]
              
print(char,maxCount)
        
        
    
