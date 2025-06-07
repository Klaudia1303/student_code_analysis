s = input('> ')
dist: int = 0
for c in s:
    if s.count(c) > 1:
        d: int = s.rfind(c) - s.find(c)
        if d > dist:
            dist = d
print(dist)
