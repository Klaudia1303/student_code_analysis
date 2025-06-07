s=input('inserire stringa: ')
x=0
i=0
while i<len(s):
    if s.count(s[i])>= x:
        x=s.count(s[i])
        lettera=i
    i=i+1
print(s[lettera])
