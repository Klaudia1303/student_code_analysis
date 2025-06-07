s = input('stringa = ')

dist = 0

for i in range(len(s)-1,0,-1):
    if s.rfind(s[i]) - s.find(s[i]) > dist:
        dist = s.rfind(s[i]) - s.find(s[i])

print(dist)
    
