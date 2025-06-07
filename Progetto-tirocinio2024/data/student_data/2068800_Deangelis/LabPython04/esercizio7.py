s = input("inserisci la stringa: ")
i = 0
s_max = 0
while i < len(s)-1:
    if s.count(s[i]) > s.count(s[i+1]):
        s_max = s[i]
    i += 1
print(s_max)