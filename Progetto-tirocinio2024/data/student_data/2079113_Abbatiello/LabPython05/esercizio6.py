s = input('insersci stringa:')
m = 0
for c in s:
    k = s.rfind(c) - s.find(c)
    if s.find != s.rfind(c) and m < k:
        m = k
print(m)
