s=str("alla")
n=0
for i in range(len(s)):
    if s[i] == s[len(s)-i-1]:
        n=n+1
    else:
        break

print("livello", n)
    
