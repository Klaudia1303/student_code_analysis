s = input("Stringa: ")
finito = s == s[::-1]
while not finito:
    s = input("non palindroma, inserire una stringa palindroma: ")
    if s == s[::-1]:
        finito = True
print("stringa palindroma di lunghezza", len(s))
