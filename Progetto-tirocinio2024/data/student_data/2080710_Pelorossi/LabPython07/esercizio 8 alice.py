def A_Ex8(s1,s2):
    s=''
    if len(s1)==0 or len(s2)==0:
        return s
    else:
        for i in range(len(s1)-1):
            for j in range(len(s2)-1):
                if s1[i]==s2[j] and s1[i+1]==s2[j+1]:
                    x=s1[i]
                    y=s1[i+1]
                    s+=x
        s+=y
        return s
