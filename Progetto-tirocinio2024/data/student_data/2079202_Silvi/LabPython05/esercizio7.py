import sys
s=input("inserire una stringa: ")
for i in range (0,len(s)):
    if s.rfind(s[i], i+1)!=-1:
        print(True)
        sys.exit(0)
print(False)
