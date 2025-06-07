s=input("Inserire una stringa:  ")
k=False
for i in range(len(s)):
    if s.count(s[i])>1:
        k=True
if k==True:
    print(k)
else:
    print(k)
