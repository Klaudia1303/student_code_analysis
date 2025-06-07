s1 = input("Stringa 1: ")
s2 = input("Stringa 2: ")
n = int(input("Distanza massima: "))

s = ""
for i in range(len(s1)):
    if s1[i] in s2[max(i - n, 0):min(i + n + 1, len(s2))]:
        s += s1[i]
print(s)
