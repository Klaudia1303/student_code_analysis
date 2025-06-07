char = input("Inserisci un carattere: ")

last = input("Inserisci una stringa: ")
while last.count(char) < 2:
    last = input("Inserisci una stringa: ")

print(last.count(char))
