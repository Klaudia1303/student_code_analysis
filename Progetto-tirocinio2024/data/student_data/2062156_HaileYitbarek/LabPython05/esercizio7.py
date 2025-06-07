s=input('inserire stringa: ')
a=True
for b in range(len(s)):
    if s.count(s[b])>1:
        a=True
    else:
        a=False
print(a)
        
