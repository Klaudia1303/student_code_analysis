s1=input('inserire una stringa: ')
s2=input('inserire una stringa: ')
len_max=0
c=''
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        s=s1[i:j]
        if s in s2:
            l=j-i
            if l>=len_max:
                len_max=l
                c=s
        else:
            break
print(c)
        
