c = input("inserisci un carattere:")
s = input("inserisci stringa:")
counter = 0
lettera = 0
while counter <= 2:
    if lettera < len(s):
        if s[lettera] == c:
            counter += 1
            lettera += 1
        else:
            lettera += 1
    if lettera == len(s):
        s = input("inserisci stringa:")

print(counter)

