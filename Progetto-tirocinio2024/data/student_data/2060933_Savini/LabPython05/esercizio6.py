s=input ('inserire una stringa:')
distanza=0
for i in range(len(s)):
    if distanza < s.rfind(s[i])-i:
        distanza=s.rfind(s[i])-i
print(distanza)
