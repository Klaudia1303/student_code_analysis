s = input("Inserire una stringa: ")

MaxDistance = 0

for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == s[j]:
            if abs(s.find(s[i]) - s.rfind(s[j])) > MaxDistance:
                MaxDistance = abs(s.find(s[i]) - s.rfind(s[j]))

print(MaxDistance)