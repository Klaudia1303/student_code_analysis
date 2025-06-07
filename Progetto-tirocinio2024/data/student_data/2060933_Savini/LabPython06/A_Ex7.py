s1=input ('inserisci la prima stringa: ')
s2=input ('inserisci la seconda stringa: ')
l=0
for i in range(len(s1)):
    for k in range(len(s2)) :
        j=0
        s3=''
        while s1[i+j]==s2[k+j]:
            s3=s3+s1[i+j]
            j+=1
            if i+j>=(len(s1)) or k+j>=(len(s2)) :
                break
        if j>=l:
            l=j
            s4=s3
print(s4)
