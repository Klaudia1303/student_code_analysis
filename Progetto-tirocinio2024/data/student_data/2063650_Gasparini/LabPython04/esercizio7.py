s = input("Stringa: ")

max_occorrenze = 0
max_c = ""
for c in s:
    occorrenze = s.count(c)
    if occorrenze >= max_occorrenze:
        max_occorrenze = occorrenze
        max_c = c

print(max_c)
