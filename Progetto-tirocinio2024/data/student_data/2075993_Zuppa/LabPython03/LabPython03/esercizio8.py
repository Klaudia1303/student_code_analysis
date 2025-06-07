p=False
while not p:
    s=input('inserire la stringa senza spazi ')
    while len(s)==0:
        s=input('inserire una stringa non vuota senza spazi  ')
    if len(s)%2==0:
        if s[0:(len(s)//2)] == s[-1:-(len(s)//2)-1:-1]:
            p=True
    else:
        s1=s.replace(s[((len(s)-1)//2)],'')
        if s1[0:(len(s1)//2)] == s1[-1:-(len(s1)//2)-1:-1]:
            p=True
print('stringa palindroma è di lunghezza',len(s))
