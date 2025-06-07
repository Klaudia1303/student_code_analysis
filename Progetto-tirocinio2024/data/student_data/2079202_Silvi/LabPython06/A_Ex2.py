import sys
s=input("inserire una stringa:")
for i in range (0, len(s)):

    if s[i]==s[len(s)-i-1]:
        if i==len(s):
            print(len(s))
    else:
        print("livello ",i)
        sys.exit(0)

print("livello:",len(s))
