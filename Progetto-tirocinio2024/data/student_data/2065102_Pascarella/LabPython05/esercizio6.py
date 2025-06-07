s=input()
distanza=0

for i in range(0, len(s)-1):
    if distanza+1<s.rfind(s[i]):
        distanza=s.rfind(s[i])        

print(distanza)
