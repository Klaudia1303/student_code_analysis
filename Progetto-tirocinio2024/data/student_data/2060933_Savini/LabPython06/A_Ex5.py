s= input ('inserisci la stringa: ')
n=0
c=-1
for i in range(len(s)):
    if i==len(s)-1:
        break
    if s[i]==s[i+1]:
        n+=1
    if n>=c and (s[i]!=s[i+1] or i==len(s)-2) :
        c=n
        l=i-1
        n=0
if i==len(s)-1:
    print (s [l], c+1)
else:
    print (s[l], c)
