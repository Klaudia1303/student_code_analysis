s=input('inserire una stringa:')
if len(s)==0:
    s=input('errato,inserire una stringa non vuota:')
ss=input('inserire una stringa:')
if len(ss)==0:
    ss=input('errato,inserire una stringa non vuota:')
s1=''
s2=''
s1=s
s2=ss
while s1[-1]!=s2[0]:
    s1=s2
    s2=input('inserire una stringa:')
    if len(s2)==0:
        s2=input('errato,inserire una stringa non vuota:')
print(s1,s2)
    
