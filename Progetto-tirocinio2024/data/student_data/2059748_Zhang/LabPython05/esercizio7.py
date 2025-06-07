s=input("scrivi una stringa: ")
x=set()

for i in range(len(s)):
    n=s.count(s[i])
    x.add(n)
if max(x)>1:
    print(True)
else:
    print(False)
