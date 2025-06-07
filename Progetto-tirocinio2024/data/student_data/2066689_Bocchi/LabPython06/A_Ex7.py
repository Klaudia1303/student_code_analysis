s1=input('inserire una stringa: ')
s2=input('inserire una seconda stringa: ')
y=''
for i in range(0,len(s1)):
    x=''
    for j in range(i+1,len(s1)+1):
        if s1[i:j+1] in s2:
            x=s1[i:j+1]
        else:
            break
        if len(x)>=len(y):
            y=x
            
print(y)
