s=input()
distanza =0
for i in range(0,len(s)):
    if distanza<=s.rfind(s[i])-i:
        distanza=s.rfind(s[i])-i
print(distanza)
