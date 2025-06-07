c=0
s1=input('inserire una stringa: ')
s2=input('inserire una stringa: ')
i=0
l=len(s)
st=0
st=str(st)
for c in range(l):
    if st=='0':
        if str(s1[i])!=str(s2[i]):
            st=str(s1[i])
            i+=1
            c+=1
        else:
            i+=1
            c+=1
    else:
        if str(s1[i])!=str(s2[i]):
            st=str(st)+str(s1[i])
            i+=1
            c+=1
        else:
            i+=1
            c+=1
print(st)
    
