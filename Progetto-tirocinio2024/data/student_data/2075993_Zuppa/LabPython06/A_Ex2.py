s=input('inserire una stringa  ')
s0=s[len(s)-1:(len(s)//2)-1:-1]
c=0
p=True
for i in range(len(s)//2):
    if s[i]==s0[i]:
        c+=1
    else:
        p=False
        break
if p:
    print('stringa palindroma di livello :',len(s))
else:
    print('stringa palindroma di livello :',c)
