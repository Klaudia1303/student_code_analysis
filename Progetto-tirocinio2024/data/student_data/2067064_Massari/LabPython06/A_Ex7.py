s1=input('inserire la prima stringa: ')
s2=input('inserire la seconda stringa: ')
parola=''
s1=s1+'*'
s2=s2+'*'
if len(s1)>0 and len(s2)>0:
    for i in range(len(s1)):
        if s1[i]=='*':
            print(parola)
            break
        for j in range(len(s2)):
                if s1[i]==s2[j]:
                    if s1[i-1]==s2[j-1]:
                        parola+=s2[j]
                    if s1[i-1]!=s2[j-1] and s1[i+1]=='*' or s2[j+1]=='*':
                        continue
                    if s1[i-1]!=s2[j-1] and s1[i+1]==s2[j+1]:
                        parola+=s2[j]
