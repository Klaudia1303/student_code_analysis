s=str(input('inserire stringa: '))
n1=-1

for c in range(len(s)):
    
    if s.rfind(s[c])!=s.find(s[c]):
        n= int(s.rfind(s[c]))-int(s.find(s[c]))
        
        if n1<n:
            n1=n

if n1>-1:
    print(n)

else:
    print('0')
