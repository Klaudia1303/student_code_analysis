s=  input("")

lev= len(s)
revd= s[::-1]

acc=0

for i in range(lev//2+1):
    if s[i]==revd[i]:
        acc +=1
        
    elif s[i]!=revd[i]:
        print(acc)
        exit
