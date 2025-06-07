s=input("Inserire una stringa:")
c=0
mass=0
mass2=0
v=''
k=''
if s=='':
    print("mancanza stringa")
else:
    while c<len(s):
        i=s[c]
        s.count(i)
        if mass<s.count(i):
            mass=s.count(i)
            v=s[c]
        if mass==s.count(i):
            mass2=0
            k=s[c]
        c+=1
    if s.find(v)>s.find(k):
        print(v)
    else:
        print(k)
