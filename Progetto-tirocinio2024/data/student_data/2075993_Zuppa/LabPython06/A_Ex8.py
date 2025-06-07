s1=input('inserire una stringa  ')
s2=input('inserire una stringa  ')
n=int(input('inerire un intero   '))
c=False
s=''
for i in range(len(s1)):
    if s1[i] in s2:
        for j in range(1,n):
            if s1[i+j]in s2:
                c=True
                s+=s1[i]
                s+=s1[i+j]
                break
        if c:
            break
print(s)
            
                
