s=input('inserire una stringa non vuota   ')
while len(s)==0:
    s=input('inserire una stringa non vuota   ')
M=0
c=0
for i in range(len(s)):
    if c<=s.count(s[i]):
        c=s.count(s[i])
        M=s[i]
print(M,c)
