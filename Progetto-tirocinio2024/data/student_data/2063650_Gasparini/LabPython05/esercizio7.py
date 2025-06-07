s = input("Stringa: ")

presente = False;
for c in s:
    if s.count(c) > 1:
        presente = True
        break
print(presente)
