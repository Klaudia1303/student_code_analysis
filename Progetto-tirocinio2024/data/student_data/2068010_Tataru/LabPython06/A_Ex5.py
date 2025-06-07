s=input()
mc=1
ch=s[0]
if(len(s)==2 and s[0]!=s[1]):
    ch=s[1]
    s=s[1:len(s)]
while (len(s)>1):
    c=1
    while (s[0]==s[1]):
        c+=1
        s=s[1:len(s)]
        if (c>=mc):
            ch=s[0]
            mc=c
        if(len(s)==1):
            break
    s=s[1:len(s)]
print(ch,mc)
