s=str(input("Inserire una stringa:"))
for i in range(len(s)):
    if s.count(s[i])>=2:
        find=s.find(s[i])
        rfind=s.rfind(s[i])
        distanza=rfind-find
if distanza>0:
    print(distanza)
else:
    print(0)
