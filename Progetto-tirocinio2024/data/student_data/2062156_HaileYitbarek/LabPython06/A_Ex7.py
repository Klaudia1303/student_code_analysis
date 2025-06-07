s1=input('inserire stringa non vuota: ')
s2=input('inserire stringa non vuota: ')
a=(0,0)
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        if s1[i:j] in s2:
            if j-i>a[1]-a[0]:
                a=(i,j)
        else:
            break
print(s1[a[0]:a[1]])
        
