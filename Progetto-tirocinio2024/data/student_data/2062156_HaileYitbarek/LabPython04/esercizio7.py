s=input('inserire stringa: ')
a=1
massimo=s.count(s[0])
while a<len(s):
    if s.count(s[a])>=massimo:
        massimo=s.count(s[a])
        a=a+1
    else:
        a=a+1
b=True
c=a-1
while b:
    if s.count(s[c])==massimo:
        print(s[s.rfind(s[c])])
        b=False
    else:
        c=c-1
    
    
    
