s=input('inserire una stringa: ')
k=0
for i in range(0,len(s)):
    x=s.rfind(s[i])
    if x-i>k:
        k=x-i
print(k)
    
    
