s=input('inserire una stringa    ')
while len(s)==0:
    s=input('inserire una stringa non vuota   ')
M=0
e=''
c=len(s)-1
while c!=0 :
    if M<s.count(s[c]):
        M=s.count(s[c])
        if e != s[c] and s.rfind(e)>s.rfind(s[c]):
            e=s[c]
    c-=1
print('l elemento che compare più volte è:',e)
