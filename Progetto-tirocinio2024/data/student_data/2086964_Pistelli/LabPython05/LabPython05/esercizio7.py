s=input('inserire una stringa ')
A=set()
for i in range(len(s)):
    m=s.count(s[1])
    A.add(m)
if max(A)>1:
    print(True)
else:
    print(False)
