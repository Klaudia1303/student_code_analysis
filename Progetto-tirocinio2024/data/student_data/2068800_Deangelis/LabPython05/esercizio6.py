s = input("inserisci la stringa: ")
dist = 0
for i in range(len(s)):
    if dist < s.rfind(s[i])-i:
        dist = s.rfind(s[i])-i
print(dist)