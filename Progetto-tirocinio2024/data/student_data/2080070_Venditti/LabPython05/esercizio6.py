s=input('iserire una stringa: ')
x=0
for i in range(len(s)):
    if x<s.rfind(s[i])-i:
        x=s.rfind(s[i])-i
        print(x)
