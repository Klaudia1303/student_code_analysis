r=1
s=input("inserire una stringa: ")
c=input("inserire una stringa: ")
l=input("inserire una stringa: ")
while r!=2:
    if (len(s)+len(c)==len(l)) and r!=2:
        print(s,c,l)
        r+=1
    if r!=2:
        s=input("inserire una stringa: ")
    if (len(c)+len(l)==len(s)) and r!=2:
        print(c,l,s)
        r+=1
    if r!=2:
        c=input("inserire una stringa: ")
    if (len(l)+len(s)==len(c)) and r!=2:
        print(l,s,c)
        r+=1
    if r!=2:
        l=input("inserire una stringa: ")
