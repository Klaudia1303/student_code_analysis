s=input('Inserire una stringa: ')
x=0
for i in range(len(s)):
    if s.rfind(s[i])-i>x:
        x=s.rfind(s[i])-i
print(x)
