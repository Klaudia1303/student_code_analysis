s = input("stringa: ")
distanza = 0

for i in range(len(s)):
    nuova_dist = s.rfind(s[i]) - i
    if nuova_dist > distanza:
        distanza = nuova_dist

print(distanza)
