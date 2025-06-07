

s1=input("Inserire stringa:\t")
s2=input("Inserire stringa:\t")
s=""

for a in range(len(s1)):
    for b in range(a+1,len(s1)+1):
        p=s1[a:b]
        if p in s2 and not(p in s):
            
            if len(p)>len(s):
                s=p
print(s)
