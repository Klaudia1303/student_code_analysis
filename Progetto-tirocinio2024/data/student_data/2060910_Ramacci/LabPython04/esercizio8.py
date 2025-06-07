r=0
p=0
while r!=1:
    while p<1:
        s=input("inserire una stringa: ")
        t=str(s)
        q=str("")
        p+=1
        while p>=1 and r!=1:
            m=input("inserire una stringa: ")
            q=str(m)
            if q[0]==t[-1]:
                print(t,q)
                r+=1
            s=input("inserire una stringa: ")
            t=str(s)
            if q[-1]==t[0]:
                print(q,t)
                r+=1
