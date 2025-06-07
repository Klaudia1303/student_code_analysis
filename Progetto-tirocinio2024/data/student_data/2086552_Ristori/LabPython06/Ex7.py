s1=str(input("Inserire la prima stringa:"))
s2=str(input("Inserire la seconda striga:"))
risPrec=''
risAt=''
for i in range(len(s1)):
    for j in range(len(s2)):
        if j>=len(s2)-1:
            break
        if s1[i]==s2[j]:
            risAt=s1[i]
            for z in range(i+1,len(s1)):
                if s1[z]==s2[j+1]:
                    risAt+=s1[z]
                    j+=1
                    if j>=len(s2)-1:
                        break
                else:
                    break
    if len(risAt)>=len(risPrec):
        risPrec=risAt
        risAt=''
print(risPrec)

                    
