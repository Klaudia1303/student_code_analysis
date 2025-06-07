s=input('inserire una stringa: ')
x=0
for i in range(len(s)):
    i=s[i]
    if s.count(i)>1:
        x+=1
if x!=0:
    print(True)
else:
    print(False)
