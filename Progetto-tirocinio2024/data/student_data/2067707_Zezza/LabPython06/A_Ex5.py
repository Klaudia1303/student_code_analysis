s=input('stringa alfanumerica: ')
n=1
k=0
s+=' '
for i in range(1,len(s)-1):
    while s[i-1]==s[i]:
        n+=1
        i+=1
        if n>=k:
            k=n
            c=s[i-1]
    n=1
print(k,c)
