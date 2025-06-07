s = input("Inserire una stringa:")
i = 0
for x in s:
    d = abs(s.find(x) - s.rfind(x))
    if d >= i:
        i = d
print(i)
