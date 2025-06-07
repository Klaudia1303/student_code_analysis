s=str(input('inserire una stringa: '))
q=str(input('inserire una stringa; '))
n=int(input('inserire un intero: '))
a=''
for i in range(len(s)):
    if s[i] in q:
        if s[i] not in a:
            if i==len(s)-1:
                break
            elif i==0:
                continue
            else:
                a=a+s[i]
                for j in range(i-n,i):
                    if s[j] in q:
                        a=a+s[j]
                for j in range(i+1,i+n+1):
                    if s[j] in q:
                        a=a+s[j]