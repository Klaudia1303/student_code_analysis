s=input('inserisci una stringa alfanumerica non vuota')
d=1
f=0
a='*'
for i in range (1,len(s)):
    if s[i-1]==s[i]:
        d+=1
    else:
        d=1
    if d>=f:
        f=d
        a=s[i]
   
print (a,f)

