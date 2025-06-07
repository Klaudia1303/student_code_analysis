s=input()
v=[]
l=[]
for i in range(0,25):
    v.append(0)
s=s.upper()
for i in s:
    v[ord(i)-65]+=1
m=max(v)
while(max(v)==m):
    l.append(chr(v.index(m)+65))
    v[v.index(m)]=0
con=True
for i in range(len(s)-1,0,-1):
    for j in l:
        if(s[i]==j):
            print(j.lower())
            con=False
            break
    if (con==False):
        break
