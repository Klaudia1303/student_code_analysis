s=str(input("scrivi una stringa: "))
x=0
if s[0]==s[-1]:
    x=1
y=len(s)-2
for i in range(len(s)//2):
    if s[::-1]==s:
        print(len(s))
        break
    if s[i]==s[y]:
        x+=1
        i+=1
        y-=1
if s[::-1]!=s:
    print(x)
