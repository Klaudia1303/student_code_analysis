st1=input('inserire una parola: ')
i=1
s=0
a=str('a')
c=str('c')
while (i==1):
    if (st1.find(a)  and st1.find(c)):
        s+=1
        st1=input('inserire una parola: ')
    else:
        s+=1
        i=0
print(s)
