i=0
x=0
while i!=1:
    while x<1:
        s=input("scrivi una stringa non vuota: ")
        a=str(s)
        b=str('')
        x+=1
        while x>=1 and i!=1:
            s=input("scrivi una stringa non vuota: ")
            b=str(s)
            if b[0]==a[-1]:
                print(a,b)
                i+=1
            s=input("scrivi una stringa non vuota: ")
            a=str(s)
            if b[-1]==a[0]:
                print(b,a)
                i+=1
