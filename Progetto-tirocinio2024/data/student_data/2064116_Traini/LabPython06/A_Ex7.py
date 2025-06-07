s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
c=''
a=''
for i in s1:
    c=i
    for k in s1:
        if s2.count(c)>0:
            if s2.count(c+k)>0 and s1.count(c+k)>0:
                c=c+k
                if len(c)>=len(a):
                    a=c
            elif (a=='' or len(a)==1) and s2.count(c)>0:
                a=c
        else:
            break
print(a)
