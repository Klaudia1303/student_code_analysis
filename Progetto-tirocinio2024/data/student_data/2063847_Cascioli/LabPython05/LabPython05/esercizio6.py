s=input("Inserire una stringa")
dist_max=0
for i in range (len(s)):
    dist=s.rfind(s[i])-i
    if (dist>dist_max):
        dist_max=dist
print(dist_max)
