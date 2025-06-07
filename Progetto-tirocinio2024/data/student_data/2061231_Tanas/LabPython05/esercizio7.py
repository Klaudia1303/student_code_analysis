s = input("stringa: ")

trovato = False
for c in s:
    if s.count(c) > 1:
        trovato = True

print(trovato)
