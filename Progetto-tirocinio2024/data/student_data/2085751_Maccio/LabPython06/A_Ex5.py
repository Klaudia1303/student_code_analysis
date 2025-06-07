s=input("Inserire una stringa:  ")
a=""
g=1
p=0
s+=" "
for i in range(0,len(s)):
        while s[i-1]==s[i]:
            g=g+1
            i+=1
            if g>=p:
                a=s[i-1]
                p=g
        g=1
print(a,p)

