s=input('inserire stringa:')
for i in range(len(s)):
    if s.find(s[i])!=s.rfind(s[i]):
        print(True)
        break
if s.find(s[i])==s.rfind(s[i]):
    print(False)
