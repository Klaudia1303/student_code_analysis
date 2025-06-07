s=input("inserire stringa alfanumerica : ")
k=1 
a=1 
if len(s)!=1 and len(s)!=2:
    for i in range (len(s)):
        x=s.count(s[i])
        if x>k:
            y=s[i]
            k+=1
        
    for p in range (s.find(y),len(s)):
        x2=s.count(s[p])
        if x2==x :
            y=s[p]

    for t in range (len(s)-2):
        if s[t]==s[t+1]:
            a+=1
            z=s[t]
            if s[-2]==s[-1]:
                a+=1
    print(y, s.count(y))

else:
    if len(s)==1:
        print(s[0],'1')
    else:
        if s[0]==s[1]:
            print(s[0],'2')
        else:
            print(s[1],'1')
