s=input("Inserisci una stringa: ")
n=0
l=0
a=False
if len(s)==2 and s[0]==s[1]:
    print(s[0],2)
elif len(s)==1:
    print(s[0],1)
elif len(s)>2:
    for k in range(0, len(s)-1):
        if s[k]==s[k+1]:
            a=True
            break
    for i in range(len(s)-1):
        if i+n<=len(s):
            if s[i]==s[i+1] and s[i+abs(n-1)] == s[i]:
                n=1
                l=i
                for j in range (len(s)-i):
                    if s[i+j]==s[i] and s[i+j]==s[i+j-1]:
                        n+=1
    if a:
        print(s[l],n)
    else:
        print(s[i+1],1)
