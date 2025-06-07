s = input('Inserisci stringa: ')
max_dist = 0

for i in range(len(s)):
    dist = s.rfind(s[i])-i
    if dist > max_dist:
        max_dist = dist
print(max_dist)
