last = input("Inserisci una stringa: ")

while not last.isalpha() or not last.islower():
    print(last[0] + last[len(last) - 1])
    last = input("Inserisci una stringa: ")

print(last[0] + last[len(last) - 1])
