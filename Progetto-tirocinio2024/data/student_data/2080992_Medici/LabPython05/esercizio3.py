s1=str(input('inserire una stringa: '))
s2=str(input('inserire una stringa: '))
s=''
for i in s1:
    b=1
    for j in s2:
        if i==j:
            b=0; break
    if b==1:
        s+=i
print(s)
