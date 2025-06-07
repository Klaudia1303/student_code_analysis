s = ''
while len(s) == 0:
    s = input("stringa alfanumerica: ")

max_c = ''
max_l = 0

for c in s:
    temp_l = s.count(c)

    if temp_l >= max_l:
        max_c = c
        max_l = temp_l

print(max_c, max_l)