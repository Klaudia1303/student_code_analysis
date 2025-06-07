s=input('inserire una stringa: ')
n=len(s)
i=0
c=0
lett=0
par=0
while (i<=n):
    lett=str(s.find(s[i:0]))
    c=s.count(lett)
    i+=1
    if (par<=c):
        par=c
print(par)
