s1=input("scivi una stringa: ")
s2=input("scrivi una stringa: ")
s=''

for i in range(len(s1)):
    st=''
    c=i
    for j in range(len(s2)):
        if c>=len(s1):
            break
        if s1[c]==s2[j]:
            st+=s1[c]
            if len(st)>len(s):
                s=st
            if j<=len(s2)-1:
                c+=1
        elif len(st)>0:
            st=''
            c=i

print(s)
            
    
