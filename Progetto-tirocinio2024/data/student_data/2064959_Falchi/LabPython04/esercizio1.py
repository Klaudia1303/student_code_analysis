s = input("Immettere stringa: ")
str_count = 0

if not (s.count('a') > 0 and s.count('c') > 0):
    str_count += 1

    while not (s.count('a') > 0 and s.count('c') > 0):
        s = input("Immettere stringa: ")
        str_count += 1

print(str_count)
