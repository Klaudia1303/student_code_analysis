s=input()
n=int(input())
for i in range(len(s)-n):
    if s[i]==s[i+n]:
        print(True)
        break
else: print(False)